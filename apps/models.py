"""
models.py

"""

from apps import db


class User(db.Model):
<<<<<<< HEAD
    email = db.Column(db.String(255), primary_key = True)
    password = db.Column(db.String(255))
    name = db.Column(db.String(255))
=======
    email = db.Column(db.String(225), primary_key = True)
    password = db.Column(db.String(225))
    name = db.Column(db.String(225))
>>>>>>> origin/phk
    join_date = db.Column(db.DateTime(), default=db.func.now())

class Article(db.Model):
    id = db.Column(db.Integer, primary_key = True)
<<<<<<< HEAD
    title = db.Column(db.String(255))
    content = db.Column(db.Text())
    author_id = db.Column(db.String(255), backref=db.backref(''))
    category = db.Column(db.String(255))
=======
    title = db.Column(db.String(225))
    content = db.Column(db.Text())
    author = db.Column(db.String(225))
    category = db.Column(db.String(225))
>>>>>>> origin/phk
    date_created = db.Column(db.DateTime(), default=db.func.now()) # DateTime (save time)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'))
    article = db.relationship('Article', backref=db.backref('comments', cascade='all, delete-orphan', lazy='dynamic'))
    # cascade -> article delete = comments delete
    # data base tuning!

<<<<<<< HEAD
    author = db.Column(db.String(255))
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
=======
    author = db.Column(db.String(225))
    email = db.Column(db.String(225))
    password = db.Column(db.String(225))
>>>>>>> origin/phk
    content = db.Column(db.Text())
    date_created = db.Column(db.DateTime(), default=db.func.now())





