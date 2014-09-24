# -*- coding: utf-8 -*-
"""
models.py

"""



from apps import db

class User(db.Model):
    email = db.Column(db.String(255),primary_key=True)
    password=db.Column(db.String(255))
    join_date=db.Column(db.DateTime(), default=db.func.now())
    user_nick= db.Column(db.String(20))