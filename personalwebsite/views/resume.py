"""
Insta485 index (main) view.

URLs include:
/
"""
import uuid
import hashlib
import pathlib
import arrow
from flask import abort, session, render_template, redirect, url_for
from flask import request, send_from_directory
import personalwebsite


@personalwebsite.app.route('/resume/')
def show_resume():
    """Send resume."""
    resume_path = pathlib.Path(__file__).resolve().parent.parent/"static"/"files"
    return send_from_directory(resume_path, "resume.pdf", as_attachment=True)
