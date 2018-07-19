from .base import *

DEBUG = True
ALLOWED_HOSTS = []

# Static
# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(ROOT_DIR, '.static')
# EC2_DEPLOY = os.path.dirname(BASE_DIR)
# MEDIA_ROOT = os.path.join(EC2_DEPLOY,'.media')
# MEDIA_URL ='/media/'

# wsgi
WSGI_APPLICATION = 'config.wsgi.local.application'

# DB
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_URL = '/static/'


# LOG_DIR = os.path.join(ROOT_DIR, 'log') #이부분 왜 애러뜨지?
# LOG_DIR='/var/log/'
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'filters': {
#         'require_debug_false': {
#             '()': 'django.utils.log.RequireDebugFalse',
#         },
#         'require_debug_true': {
#             '()': 'django.utils.log.RequireDebugTrue',
#         },
#     },
#     'formatters': {
#         'django.server': {
#             'format': '[%(asctime)s] %(message)s',
#         }
#     },
#     'handlers': {
#         'console': {
#             'level': 'INFO',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#         },
#         'file_error': {
#             'class': 'logging.handlers.RotatingFileHandler',
#             'level': 'ERROR',
#             'formatter': 'django.server',
#             'backupCount': 10,
#             'filename': os.path.join(LOG_DIR, 'error.log'),
#             'maxBytes': 10485760,
#         }
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console', 'file_error'],
#             'level': 'INFO',
#             'propagate': True,
#         }
#     }
# }