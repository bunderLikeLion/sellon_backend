from os.path import join

from .base import * # noqa pylint: disable=wildcard-import, unused-wildcard-import

DEBUG = True
ALLOWED_HOSTS = ['*']
PROJECT_DIR = environ.Path(__file__) - 3

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

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'fileFormat': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s',
            'datefmt': '%d/%b/%Y %H:%M:%S'
        }
    },
    'handlers': {
        'sql_logger': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': join(PROJECT_DIR, 'logs/sql_logfile.log'),
            'formatter': 'fileFormat'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': join(PROJECT_DIR, 'logs/logfile.log'),
            'formatter': 'fileFormat'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },

    },
    'loggers': {
        'simple_loger': {
            'handlers': ['console', 'file'],
            'level': 'INFO'
        },
        'django.db.backends': {
            'handlers': ['console', 'sql_logger'],
            'level': 'DEBUG',
        },
    },
}
