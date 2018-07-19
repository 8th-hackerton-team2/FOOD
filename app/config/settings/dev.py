from .base import *

secrets = json.load(open(os.path.join(SECRET_DIR, 'dev.json')))

DEBUG = True
ALLOWED_HOSTS = []


# django-storages
INSTALLED_APPS += [
    'storages',
    'django_extensions',
]

# AWS
AWS_ACCESS_KEY_ID = secrets['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = secrets['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = secrets['AWS_STORAGE_BUCKET_NAME']
AWS_DEFAULT_ACL = secrets['AWS_DEFAULT_ACL']
AWS_S3_REGION_NAME = secrets['AWS_S3_REGION_NAME']
AWS_S3_SIGNATURE_VERSION = secrets['AWS_S3_SIGNATURE_VERSION']


# wsgi
WSGI_APPLICATION = 'config.wsgi.dev.application'

# DB
DATABASES = secrets['DATABASES']

STATIC_URL = '/static/'

# MEDIA
DEFAULT_FILE_STORAGE = "config.storages.S3DefaultStorage"
# STATICFILES_STORAGE = 'config.storages.S3StaticStorage'

print(DATABASES)