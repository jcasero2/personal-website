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


@personalwebsite.app.route('/')
def show_index():
    """Home Page of personalwebsite."""
    context = {}
    return render_template("index.html", context=context)
