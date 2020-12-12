from .base import *
DEBUG = False
ADMINS = (
 ('Vishwajit', 'vishwajit20bhagat@gmail.com'),
)
ALLOWED_HOSTS = ['*']
DATABASES = {
 'default': {
 'ENGINE': 'django.db.backends.postgresql',
 'NAME': 'education',
 'USER': 'postgres',
 'PASSWORD': '1234',
 }
}
SECURE_HSTS_SECONDS = 3600
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_INCLUDE_SUBDOMAINS=True
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE =True
SECURE_HSTS_PRELOAD=True