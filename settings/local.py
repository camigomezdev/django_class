from .base import *

DEBUG = True

ALLOWED_HOSTS = ['localhost']
INSTALLED_APPS.append('debug_toolbar')
MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')
INTERNAL_IPS = ['127.0.0.1']

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "amigurumis_db",
        "USER": "root",
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
