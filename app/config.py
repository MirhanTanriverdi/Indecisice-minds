import os
from dotenv import load_dotenv
from os import environ
# basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv()

SECRET_KEY = os.environ.get('SECRET_KEY') or 'my-secret-key'
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
#SQLALCHEMY_TRACK_MODIFICATIONS = False

