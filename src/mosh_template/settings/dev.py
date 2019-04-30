from .base import *

DATABASES = {
    'default': {
        'ATOMIC_REQUESTS': True,
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PW'),
        'TEST': {
            'NAME': f'test_{config("DB_NAME")}',
        },
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': '',
    }
}

INSTALLED_APPS.extend(['django_extensions', 'health_check.storage', ])

TOOLBAR = False

if TOOLBAR:
    INTERNAL_IPS = ['localhost', '127.0.0.1', ]

    INSTALLED_APPS.append('debug_toolbar')

    MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')

    DEBUG_TOOLBAR_CONFIG = {
        'DISABLE_PANELS': {
            'debug_toolbar.panels.redirects.RedirectsPanel'
        },
        'JQUERY_URL': os.path.join(BASE_DIR, 'static/js/jquery-3.3.1.min.js'),
    }

LOGGER = False

if LOGGER:
    import logging

    INSTALLED_APPS.append('nplusone.ext.django')

    MIDDLEWARE.append('nplusone.ext.django.NPlusOneMiddleware')

    NPLUSONE_LOGGER = logging.getLogger('nplusone')
    NPLUSONE_LOG_LEVEL = logging.WARN

    LOGGING = {
        'version': 1,
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
            },
        },
        'loggers': {
            'nplusone': {
                'handlers': ['console'],
                'level': 'WARN',
            },
        },
    }
