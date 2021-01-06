from .base import *

DEBUG=True
ALLOWED_HOSTS = ['.educaproject.localhost']
DATABASES={
    "default":{
        "ENGINE":'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
# from .base import *
# DEBUG = False
# ADMINS = (
#  ('Vishwajit', 'vishwajit20bhagat@gmail.com'),
# )
# ALLOWED_HOSTS = ['*']
# DATABASES = {
#  'default': {
#  'ENGINE': 'django.db.backends.postgresql',
#  'NAME': 'educa',
#  'USER': 'educa',
#  'PASSWORD': '1234',
#  }
# }

