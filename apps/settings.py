"""
settings.py

Configuration for Flask app

"""
import os
from datetime import timedelta

class Config(object):
    # Set secret key to use session
    SECRET_KEY = "musicool123890"
    debug = False
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=10)


class Production(Config):
    debug = True
    CSRF_ENABLED = False
    ADMIN = "musicoollion@gmail.com"
    SQLALCHEMY_DATABASE_URI = 'mysql+gaerdbms:///blog?instance=musicool-spk-123:musicool'
    migration_directory = 'migrations'
