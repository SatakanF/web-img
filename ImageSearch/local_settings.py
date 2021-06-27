import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-c#+my2dtphap$zvon5-$07(x(3obdc*d959&xvv9bb9qgbe#9m'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_uks_images',
        'USER': 'root',
        'PASSWORD': 'uksretail2021',
        'HOST': 'localhost',
    }
}


STATIC_DIR = os.path.join(BASE_DIR,'static')
STATICFILES_DIRS = [STATIC_DIR]