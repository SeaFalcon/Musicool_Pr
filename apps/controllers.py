# -*- coding: utf-8 -*-
from flask import render_template, request, url_for, redirect, flash, session, g, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import desc
from apps import app, db
from apps.models import (
    Article,
    Comment,
    User
)
from flask_wtf import Form
from wtforms import (
    StringField,
    PasswordField,
    TextAreaField,
)

from wtforms import validators
from wtforms.fields.html5 import EmailField

@app.route('/')
def show_home():
    return render_template('home.html')

@app.route('/makemusic')
def makemusic():
    return render_template('index.html')