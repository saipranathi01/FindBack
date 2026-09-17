from app import app, DATABASE_FILE, FOUND_UPLOAD_DIR, LOST_UPLOAD_DIR
from PIL import Image, ImageDraw
import sqlite3
import uuid

c = app.test_client()

for p in ['/', '/found', '/register', '/login', '/dashboard']:
    r = c.get(p, follow_redirects=False)
    print(p, r.status_code)

FOUND_UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
LOST_UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

img1 = Image.new('RGB', (20, 20), color='white')
img2 = Image.new('RGB', (20, 20), color='white')
d1 = ImageDraw.Draw(img1)
d1.rectangle((2, 2, 8, 8), fill='black')
d2 = ImageDraw.Draw(img2)
d2.rectangle((2, 2, 8, 8), fill='black')
img1.save(str(FOUND_UPLOAD_DIR / 'fixture_found.png'))
img2.save(str(LOST_UPLOAD_DIR / 'fixture_lost.png'))

email = 'claimer_' + str(uuid.uuid4())[:8] + '@example.com'
r = c.post('/register', data={'name': 'Verified Claimer', 'email': email, 'password': 'claim123', 'confirm_password': 'claim123'}, follow_redirects=False)
print('register', r.status_code, r.location)

r = c.post('/login', data={'email': email, 'password': 'claim123'}, follow_redirects=False)
print('login', r.status_code, r.location)

r = c.post('/found/report', data={
    'item_name': 'Blue Mug',
    'category': 'Cup',
    'location': 'Library Hall',
    'description': 'Blue ceramic mug with logo.',
    'photo': (open(str(FOUND_UPLOAD_DIR / 'fixture_found.png'), 'rb'), 'fixture_found.png'),
    'question1': 'What color handle?',
    'answer1': 'blue',
    'question2': 'What logo?',
    'answer2': 'LostLink',
    'question3': 'Where is mark?',
    'answer3': 'bottom',
}, content_type='multipart/form-data', follow_redirects=False)
print('found_report', r.status_code, r.location)

r = c.post('/lost/report', data={
    'item_name': 'Blue Mug',
    'category': 'Cup',
    'description': 'Missing a mug. I had blue ceramic mug.',
    'photo': (open(str(LOST_UPLOAD_DIR / 'fixture_lost.png'), 'rb'), 'fixture_lost.png')
}, content_type='multipart/form-data', follow_redirects=False)
print('lost_report', r.status_code, r.location)

conn = sqlite3.connect(DATABASE_FILE)
conn.row_factory = sqlite3.Row
found_id = conn.execute("SELECT id FROM found_items WHERE item_name='Blue Mug' ORDER BY id DESC LIMIT 1").fetchone()['id']
conn.close()

r = c.get('/start_verification/' + str(found_id), follow_redirects=False)
print('start_verification', r.status_code, r.location)

# follow redirect to verification page and parse the lost_id used in URL path
r_verify = c.get(r.location, follow_redirects=False)
print('verify_page_status', r_verify.status_code)

# read lost item id from the route redirect location path
lost_id = int(r.location.split('/')[-1])

r = c.post('/verify/' + str(found_id) + '/' + str(lost_id), data={'q1': 'blue', 'q2': 'LostLink', 'q3': 'bottom'}, follow_redirects=False)
print('verify_post', r.status_code, r.location)

r_success = c.get(r.location, follow_redirects=False)
print('verify_success_get', r_success.status_code)

r_claim = c.post('/claim/create/' + str(found_id) + '/' + str(lost_id), follow_redirects=False)
print('claim_create', r_claim.status_code, r_claim.location)

r = c.get('/claims', follow_redirects=False)
print('claims', r.status_code)

r = c.get('/dashboard', follow_redirects=False)
print('dashboard', r.status_code)

r = c.get('/found', follow_redirects=False)
html = r.get_data(as_text=True)
print('private leakage check', 'Red keychain' in html, 'LostLink' in html, 'left side' in html)
