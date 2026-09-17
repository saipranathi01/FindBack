# LostLink

LostLink is a privacy-preserving Lost and Found web application built with Flask, SQLite, HTML, CSS, vanilla JavaScript, and a simple local image similarity implementation using Pillow and imagehash.

## Features

- User registration and login with password hashing.
- Report found items with private photo upload and three private verification questions/answers.
- Report lost items with optional photo.
- Public found-item browsing with private photo and verification details hidden.
- Local image matching for lost photos against found-item photos.
- Ownership verification using private questions, answer normalization, and a 3-attempt limit.
- Claim submission, approval, and rejection workflow.

## Technology Stack

- Python
- Flask
- SQLite
- Pillow
- imagehash
- HTML
- CSS
- Vanilla JavaScript

## Folder Structure

```text
LostLink/
├── app.py
├── requirements.txt
├── README.md
├── database/
│   └── lostlink.db
├── private_uploads/
│   ├── found_items/
│   └── lost_items/
├── ai/
│   └── matcher.py
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── register.html
│   ├── login.html
│   ├── dashboard.html
│   ├── found_items.html
│   ├── report_found.html
│   ├── report_lost.html
│   ├── matches.html
│   ├── verify.html
│   └── claims.html
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── script.js
```

## Installation

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Windows Setup

On Windows, activate the virtual environment with:

```powershell
venv\Scripts\activate
```

Then install dependencies:

```powershell
pip install -r requirements.txt
```

## How to Run

```bash
python app.py
```

The app runs locally at:

http://127.0.0.1:5000

## Demo Data and Credentials

A sample user is created automatically by the developer instructions if needed, but you can register your own account.

Example test account:

- Email: demo@lostlink.local
- Password: demo123

You can also use the live registration page to create another account.

## How to Register

1. Open http://127.0.0.1:5000/register.
2. Enter your name, email, password, and confirm password.
3. Submit the form.

## How to Report a Found Item

1. Login.
2. Navigate to Report Found.
3. Enter item name, category, location, description, and private photo.
4. Enter exactly three private verification questions and answers.
5. Submit the form.

## How to Report a Lost Item

1. Login.
2. Navigate to Report Lost.
3. Enter item name, category, description, and optional photo.
4. Submit the form.

## How Image Matching Works

When a lost item has a photo, LostLink compares it with found-item photos by storing the photo locally in private_uploads/found_items and using a simple image hash similarity measure from Pillow and imagehash. A similarity score is created internally and stored. It is not exposed directly to end users. A potential match is created if the similarity threshold is met.

## How Ownership Verification Works

The verification page shows only the private questions. The user must answer them. The system normalizes answers case-insensitively and ignores leading/trailing spaces and repeated spaces. It compares the answer with the stored private answer. At least 2 of 3 answers must match. Up to 3 attempts total are allowed.

## How the Privacy System Works

Private photos and verification answers remain on the server in private_uploads/found_items and never appear in public found item pages. Public pages only show item name, category, location, and status.

## How to Test All Workflows

1. Register and login.
2. Report a found item with the private image and questions/answers.
3. Browse found items and ensure the photo and verification answers are not shown.
4. Report a lost item without a photo, answer a private verification question flow from found item pages, and complete claim creation.
5. Report a lost item with a photo and see a potential match in matches.
6. Create a claim and accept/reject it from the dashboard or claims page.

## Limitations

This is intentionally a simple portfolio project. Image similarity is based on average image hashes and a simple threshold, not deep AI; there is no advanced computer vision. Verification attempts are intentionally limited to three, and the UI focuses on the requested privacy-preserving lost/found workflow.
