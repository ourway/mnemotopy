# -*- coding: utf-8 -*-
import os

from .base import *

SECRET_KEY = config('SECRET_KEY')

import dj_database_url
DATABASES['default'] = dj_database_url.config()

INSTALLED_APPS += (
    'gunicorn',
    'storages',
)

ALLOWED_HOSTS = ['*']

AWS_STORAGE_BUCKET_NAME = 'mnemotopy-files'
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

STATIC_URL = ‘/static/’
STATICFILES_DIRS = (
 os.path.join(BASE_DIR, ‘static’),)
STATIC_ROOT = os.path.join(BASE_DIR, ‘staticfiles’)

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


MEDIAFILES_LOCATION = 'media'
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'mnemotopy.storages.MediaStorage'


DEBUG = False