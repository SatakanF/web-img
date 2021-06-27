from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-c#+my2dtphap$zvon5-$07(x(3obdc*d959&xvv9bb9qgbe#9m'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','91.201.39.66']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_uks_images',
        'USER': 'adminuks',
        'PASSWORD': 'uksretail2021d',
        'HOST': 'localhost',
    }
}

# STATIC_DIR = os.path.join(BASE_DIR,'static')
# STATICFILES_DIRS = [STATIC_DIR]
STATIC_ROOT = os.path.join(BASE_DIR,'stat')