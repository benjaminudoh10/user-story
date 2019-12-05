import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # Database Configuration for the application
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_FILE') or \
        'sqlite:///' + os.path.join(basedir, 'user-story-app.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'wekjdhDF@12fdjhsloiehjsgjm!@dkjn*hc^x@msdb!!&$f'
