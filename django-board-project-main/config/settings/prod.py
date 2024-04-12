import os

from .base import *

ALLOWED_HOSTS = ['*']

STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_DIRS = [
]

DEBUG = False
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']