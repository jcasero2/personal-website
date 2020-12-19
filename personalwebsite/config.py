"""Insta485 development configuration."""

import pathlib

# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/'

# Secret key for encrypting cookies
SECRET_KEY = b'\x0f\xcb\x7f7\xb8\xa1\x16t\xe6\x90i\xa4\x85\xbbH' \
                b'\xee\xf5\xfc\x9ay\x1a\x18\x9e\xe5'
SESSION_COOKIE_NAME = 'login'

# File Upload to var/uploads/
PERSONALWEBSITE_ROOT = pathlib.Path(__file__).resolve().parent.parent
UPLOAD_FOLDER = PERSONALWEBSITE_ROOT/'var'/'uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
MAX_CONTENT_LENGTH = 16 * 1024 * 1024

# Database file is var/insta485.sqlite3
DATABASE_FILENAME = PERSONALWEBSITE_ROOT/'var'/'personalwebsite.sqlite3'
