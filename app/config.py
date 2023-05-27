import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # For CSRF token
    SECRET_KEY = 'my secret key'.encode('UTF-8')
    # Protect against CSRF
    SESSION_COOKIE_SAMESITE = "Strict"
    # Protect against XSS user hijacking
    SESSION_COOKIE_HTTPONLY = True
    # Only send if HTTPS
    SESSION_COOKIE_SECURE = True
    # SQLite DB
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
