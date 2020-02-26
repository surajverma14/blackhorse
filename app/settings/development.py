from .base import *

DEBUG = True
ALLOWED_HOSTS = []
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


EMAIL_USE_TLS = True
# EMAIL_HOST = 'email-smtp.ap-south-1.amazonaws.com'
# EMAIL_HOST_USER = 'AKIAS6PTKDMT5OO4QSFH'
# EMAIL_HOST_PASSWORD = 'BO6+V2kQXjsj5Hc88YrqwBgLfADVPfD0QSrIYN2AzxZq!4'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'sv485114@gmail.com'
EMAIL_HOST_PASSWORD = 'Qwertykeypad!4'
EMAIL_PORT = 587

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
]

INSTALLED_APPS += [
    'debug_toolbar'
]

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

# DEBUG TOOLBAR SETTINGS

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]


def show_toolbar(request):
    return True


DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': show_toolbar
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STRIPE_PUBLIC_KEY = ''
STRIPE_SECRET_KEY = ''
