from os.path import join

from .base import * # noqa pylint: disable=wildcard-import, unused-wildcard-import
from config.utils import create_file_if_not_exists


DEBUG = False
ALLOWED_HOSTS = ['*']

SQL_LOG_FILE_PATH = join(PROJECT_DIR, 'logs/sql_logfile.log')
LOG_FILE_PATH = join(PROJECT_DIR, 'logs/logfile.log')

create_file_if_not_exists(str(SQL_LOG_FILE_PATH))
create_file_if_not_exists(str(LOG_FILE_PATH))

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
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': SQL_LOG_FILE_PATH,
            'formatter': 'logFormat'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': LOG_FILE_PATH,
            'filters': ['correlation_id'],
            'formatter': 'logFormat'
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'logFormat',
            'filters': ['correlation_id'],
        },

    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console', 'sql_logger'],
            'level': 'INFO',
            'formatter': 'logFormat',
            'filters': ['correlation_id'],
        },
        'django_guid': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': False,
        },
        'django': {
            'handlers': ['file', 'console'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}
