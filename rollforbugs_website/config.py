import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'rollforbugs.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True

FORTUNE_FILE = os.path.join(basedir, 'fortunes.txt')
