# -*- coding: utf-8 -*-
# all the imports

from flask import request, redirect, url_for, render_template, flash, session, g, jsonify
from apps import app, db


# , db  # db는 왜 있냐?
# from sqlalchemy import desc, asc  # 오름차순 내림차순 정렬

from sqlalchemy import desc, asc
from apps.models import User
from werkzeug.security import generate_password_hash,check_password_hash
from flask.ext.wtf import Form
from wtforms import (
    StringField,
    PasswordField,
    TextAreaField,
    IntegerField
)
from wtforms import validators
from wtforms.fields.html5 import EmailField

class joinForm(Form):
    user_nick = StringField(
        u'닉네임',
        [validators.data_required(u'이름을 입력하시기 바랍니다.')],
        description={'placeholder': u'이름을 입력하세요.'}
    )  
    email = EmailField(
        u'이메일',
        [validators.data_required(u'이메일을 입력하시기 바랍니다.')],
        description={'placeholder': u'이메일을 입력하세요.'}
    )
    password = PasswordField(
        u'패스워드',
        [validators.data_required(u'패스워드를 입력하시기 바랍니다.'),
        validators.EqualTo('confirm_password',message=u'패스워드가 일치하지 않습니다.')],
        description={'placeholder': u'패스워드를 입력하세요.'}
    )
    confirm_password = PasswordField(
        u'패스워드 확인',
        [validators.data_required(u'패스워드를 한번 더 입력하시길 바랍니다.')],
        description={'placeholder': u'패스워드를 입력하세요.'}
    )
class LoginForm(Form):
    email=EmailField(
        u'이메일',
        [validators.data_required(u'이메일을 입력하시기 바랍니다.')],
        description={'placeholder': u'이메일을 입력하세요.'}
        )
    password = PasswordField(
        u'비밀번호',
        [validators.data_required(u'패스워드를 입력하시기 바랍니다.')],
        description={'placeholder': u'패스워드를 입력하세요.'}
    )

@app.route('/')
def show_home():
    return render_template('Home.html')

@app.route('/makemusic')
def makemusic():
    return render_template('index.html')

@app.route('/user/join', methods=['GET', 'POST'])
def user_join():
    form=joinForm()
    if request.method=='POST':
        if form.validate_on_submit():
            user=User(
                    user_nick=form.user_nick.data,
                    password=generate_password_hash(form.password.data),
                    email=form.email.data
                )
            db.session.add(user) #user에 add SQL문
            db.session.commit() #user datatabase에 올림

            flash(u'시너지 회원이 된 것을 축하드립니다.', 'success')
            return redirect(url_for('show_home'))
    return render_template('User/join.html',form=form) 

@app.route('/login', methods=['GET','POST'])
def login():
    form=LoginForm()
    if request.method=='POST':
        if form.validate_on_submit():
            email=form.email.data
            pwd=form.password.data
            user=User.query.get(email) #사용자 물어보기
            if user is None:
                flash(u'존재하지 않는 id입니다.','daager')
            elif not check_password_hash(user.password,pwd):
                flash(u'패스워드가 일치하지 않습니다.', 'danger')
            else:
                session.permanent=True
                session['user_email']=user.email
                session['user_nick']=user.user_nick
            flash(u'로그인 완료.','success')
            if 'user_email' in session:
                g.user_email=session['user_email']
                g.user_nick=session['user_nick']
            return redirect(url_for('show_home'))
    return render_template('User/login.html',form=form)

@app.route('/logout')
def log_out():
    session.clear()
    return redirect(url_for('show_home'))

@app.before_request  #질문!!!
def before_request():
    g.user_email=None
    if 'user_email' in session:
        g.user_nick=session['user_nick']
        g.user_email=session['user_email']


    



    
