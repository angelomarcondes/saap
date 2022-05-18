"""
Django settings for SAAP project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

from decouple import config
from dj_database_url import parse as db_url
from easy_thumbnails.conf import Settings as thumbnail_settings
from unipath import Path
import os

BASE_DIR = Path(__file__).ancestor(1)
PROJECT_DIR = Path(__file__).ancestor(2)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

# Ativar ou desativar Django Toolbar
ENABLE_DEBUG = config('DJANGO_TOOLBAR', default=False, cast=bool)

SITE_NAME = config('SITE_NAME', default='', cast=str)
SITE_DOMAIN = config('SITE_DOMAIN', default='', cast=str)

ALLOWED_HOSTS = ['*']

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login/?next='

# SAAP_APPS business apps in dependency order
SAAP_APPS = (
    'saap.core',
    'saap.cerimonial',
    'saap.globalrules'  # manter sempre como o último da lista de apps

)

SITE_NAME = config('SITE_NAME');
SITE_DOMAIN = config('SITE_DOMAIN');

DADOS_NOME = config('DADOS_NOME');
DADOS_ENDERECO = config('DADOS_ENDERECO');
DADOS_MUNICIPIO = config('DADOS_MUNICIPIO'); 
DADOS_UF = config('DADOS_UF');
DADOS_CEP = config('DADOS_CEP');
DADOS_EMAIL = config('DADOS_EMAIL');
DADOS_TELEFONE = config('DADOS_TELEFONE');
DADOS_SITE = config('DADOS_SITE');
BRASAO_PROPRIO = config('BRASAO_PROPRIO');

VERSION='3.1.0'

INSTALLED_APPS = (
    #'django_admin_bootstrapped',
    'bootstrap_admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    #'social.apps.django_app.default',
    #'social_django',

    # more
#    'import_export',
    'smart_selects',
    'django_extensions',
    'djangobower',
    'bootstrap3',  # basically for django_admin_bootstrapped
    'crispy_forms',
    'easy_thumbnails',
    'image_cropping',
    'floppyforms',
    'sass_processor',
    'rest_framework',

    # 'haystack',
    # "elasticstack",

    'debug_toolbar',
    'taggit',
    'modelcluster',
    'easyaudit',
)

INSTALLED_APPS = INSTALLED_APPS + SAAP_APPS


# if DEBUG and 'debug_toolbar' not in INSTALLED_APPS:
#    INSTALLED_APPS += ('debug_toolbar',)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'easyaudit.middleware.easyaudit.EasyAuditMiddleware',
)

if DEBUG:
   INTERNAL_IPS = ('127.0.0.1', 'localhost', '172.27.80.68')
   MIDDLEWARE_CLASSES += (
       'debug_toolbar.middleware.DebugToolbarMiddleware',
   )

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

   DEBUG_TOOLBAR_CONFIG = {
       'INTERCEPT_REDIRECTS': False,
   }




REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    #'PAGE_SIZE': 10
}

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

ROOT_URLCONF = 'saap.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['saap/templates'],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                'django.contrib.messages.context_processors.messages',
                #'social.apps.django_app.context_processors.backends',
                #'social.apps.django_app.context_processors.login_redirect',
                'saap.context_processors.areatrabalho',
            ],
            'debug': DEBUG,
            'loaders': ['django.template.loaders.filesystem.Loader',
                        'django.template.loaders.app_directories.Loader']
        },
    },
]

WSGI_APPLICATION = 'saap.wsgi.application'

AUTH_USER_MODEL = 'core.User'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
default_dburl = 'sqlite:///{}'.format(os.path.join(PROJECT_DIR, 'db.sqlite3'))
DATABASES = {
    'default': config(
        'DATABASE_URL',
        default=default_dburl,
        cast=db_url,
    )
}


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

""" 'social.backends.twitter.TwitterOAuth' """
"""
SOCIAL_AUTH_FACEBOOK_KEY = config(
    'SOCIAL_AUTH_FACEBOOK_KEY',
    default='',
    cast=str)
SOCIAL_AUTH_FACEBOOK_SECRET = config(
    'SOCIAL_AUTH_FACEBOOK_SECRET',
    default='',
    cast=str)

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = config(
    'SOCIAL_AUTH_GOOGLE_OAUTH2_KEY',
    default='',
    cast=str)
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = config(
    'SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET',
    default='',
    cast=str)

SOCIAL_AUTH_TWITTER_KEY = config(
    'SOCIAL_AUTH_TWITTER_KEY',
    default='',
    cast=str)
SOCIAL_AUTH_TWITTER_SECRET = config(
    'SOCIAL_AUTH_TWITTER_SECRET',
    default='',
    cast=str)
"""
USER_FIELDS = ('email',)
"""
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id,name,first_name,last_name,email'
}

SOCIAL_BACKEND_INFO = {
    'facebook': {
        'title': 'Facebook',
        'icon': 'img/icon-facebook.png',
    },
    'google-oauth2': {
        'title': 'Google',
        'icon': 'img/icon-google-plus.png',
    },
}
# twitter não está funcinando com a customização do auth.User,
# ao menos localmente... testar em um domínio válido.
"""

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
LANGUAGE_CODE = 'pt-BR'
LANGUAGES = (
    ('pt-br', u'Português'),
)

TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_L10N = False
USE_TZ = True
DATE_FORMAT = 'd/m/Y'
SHORT_DATE_FORMAT = 'd/m/Y'
DATE_INPUT_FORMATS = ['%d/%m/%Y']

LOCALE_PATHS = (
    BASE_DIR.child('locale'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = PROJECT_DIR.child("collected_static")
STATICFILES_DIRS = (BASE_DIR.child("static"),)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
#    'sass_processor.finders.CssFinder',
)


MEDIA_ROOT = PROJECT_DIR.child("media")
MEDIA_URL = '/media/'

MEDIA_PROTECTED_ROOT = PROJECT_DIR.child("media_protected")

DAB_FIELD_RENDERER = \
    'django_admin_bootstrapped.renderers.BootstrapFieldRenderer'
CRISPY_TEMPLATE_PACK = 'bootstrap3'
CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap3'
CRISPY_FAIL_SILENTLY = not DEBUG

HEROKU = bool(os.environ.get('DATABASE_URL'))

BOWER_COMPONENTS_ROOT = PROJECT_DIR.child("bower")

# where to find your local bower
BOWER_PATH = '/usr/bin/bower'

if HEROKU:
    BOWER_PATH = '/app/node_modules/bower/bin/bower'

BOWER_INSTALLED_APPS = (
    'bootstrap-sass#3.3.6',
    'components-font-awesome#4.6.3',
    'tinymce#4.3.3',
    'jquery-ui#1.11.4',
    'jquery-runner#2.3.3',
    'jQuery-Mask-Plugin#1.13.4',
    'jsdiff#2.2.1',
    'https://github.com/hoarrd/drunken-parrot-flat-ui.git',
)

# Additional search paths for SASS files when using the @import statement
SASS_PROCESSOR_INCLUDE_DIRS = (
    BOWER_COMPONENTS_ROOT.child(
        'bower_components', 'bootstrap-sass', 'assets', 'stylesheets'),
)

# FIXME update cripy-forms and remove this
# hack to suppress many annoying warnings from crispy_forms

# suprime texto de ajuda default do django-filter
FILTERS_HELP_TEXT_FILTER = False


THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',
) + thumbnail_settings.THUMBNAIL_PROCESSORS

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = config('EMAIL_HOST', default='localhost')
EMAIL_PORT = config('EMAIL_PORT', cast=int, default=587)
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool, default=True)
EMAIL_SEND_USER = config('EMAIL_SEND_USER', cast=str, default='')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', cast=str, default='')
SERVER_EMAIL = config('SERVER_EMAIL', cast=str, default='')

MAX_DOC_UPLOAD_SIZE = 5 * 1024 * 1024  # 5MB
MAX_IMAGE_UPLOAD_SIZE = 2 * 1024 * 1024  # 2MB

# django-haystack: http://django-haystack.readthedocs.org/
"""
hs_eng = 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine'
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': hs_eng,
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'haystack',
    },
}
"""

"""HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': PROJECT_DIR.child('whoosh_index'),
    },
}
"""

"""HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'elasticstack.backends.ConfigurableElasticSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'haystack',
    },
}
"""

# HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
# ELASTICSEARCH_DEFAULT_ANALYZER = "snowball"

def show_toolbar(request):
    return ENABLE_DEBUG
DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK" : show_toolbar,
}

USE_DJANGO_JQUERY = True

DJANGO_EASY_AUDIT_WATCH_MODEL_EVENTS = True
DJANGO_EASY_AUDIT_WATCH_AUTH_EVENTS = True
DJANGO_EASY_AUDIT_WATCH_REQUEST_EVENTS = True
