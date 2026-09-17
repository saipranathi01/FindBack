# FindBack

FindBack is a privacy-preserving Lost and Found web application built with Flask, SQLite, HTML, CSS, vanilla JavaScript, Pillow, and imagehash.

## Features

- User registration and login with password hashing.
- Report found items with private photo upload and verification questions/answers.
- Report lost items with optional photo.
- Public found-item browsing while keeping private information hidden.
- Local image matching for lost photos against found-item photos.
- Ownership verification using private questions and answers.
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
FindBack/
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