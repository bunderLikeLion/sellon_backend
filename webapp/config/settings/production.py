from .base import * # noqa pylint: disable=wildcard-import, unused-wildcard-import

DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = (
    {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': env('POSTGRES_DB'),
            'USER': env('POSTGRES_USER'),
            'PASSWORD': env('POSTGRES_PASSWORD'),
            'HOST': 'db',
            'PORT': env('POSTGRES_PORT'),
        }
    }
)
