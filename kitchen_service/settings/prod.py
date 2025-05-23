import os

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'

ALLOWED_HOSTS = [
    '127.0.0.1',
    'kitchen-service-1yyq.onrender.com',
]

external_hostname = os.getenv('RENDER_EXTERNAL_HOSTNAME')
if external_hostname:
    ALLOWED_HOSTS.append(external_hostname)


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['POSTGRES_DB'],
        'USER': os.environ['POSTGRES_USER'],
        'PASSWORD': os.environ['POSTGRES_PASSWORD'],
        'HOST': os.environ['POSTGRES_HOST'],
        'PORT': int(os.environ['POSTGRES_DB_PORT']),
    }
}
