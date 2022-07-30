from os.path import join
from config.utils import create_file_if_not_exists
from .base import *  # noqa pylint: disable=wildcard-import, unused-wildcard-import

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

SQL_LOG_FILE_PATH = join(PROJECT_DIR, 'logs/sql_logfile.log')
LOG_FILE_PATH = join(PROJECT_DIR, 'logs/logfile.log')

create_file_if_not_exists(str(SQL_LOG_FILE_PATH))
create_file_if_not_exists(str(LOG_FILE_PATH))

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'logFormat': {
            'format': '{levelname} ... [{correlation_id}] [{name}:{lineno}] {asctime} {message}',
            'datefmt': '%d/%b/%Y %H:%M:%S',
            'style': '{',
        },

    },
    'filters': {
        'correlation_id': {
            '()': 'django_guid.log_filters.CorrelationId'
        },
    },
    'handlers': {
        'sql_logger': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': SQL_LOG_FILE_PATH,
            'formatter': 'logFormat'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': LOG_FILE_PATH,
            'filters': ['correlation_id'],
            'formatter': 'logFormat'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'logFormat',
            'filters': ['correlation_id'],
        },
        'django.server': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'filters': ['correlation_id'],
            'formatter': 'logFormat',
        },

    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console', 'sql_logger'],
            'level': 'DEBUG',
            'formatter': 'logFormat',
            'filters': ['correlation_id'],
        },
        'django_guid': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.server': {
            'handlers': ['django.server', 'file'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}
