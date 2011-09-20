import os

def rel(*x):
	return os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

MEDIA_ROOT = rel('media')

TEMPLATE_DIRS = (
	rel('templates'),
)

DATABASES = {
	'default': {'ENGINE': 'django.db.backends.sqlite3','NAME': rel('prjdb.sqlite')}
}

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('dex', 'dexter.winner@gmail.com'),
)

MANAGERS = ADMINS

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

MEDIA_URL = ''

ADMIN_MEDIA_PREFIX = '/media/'

SECRET_KEY = ')&%z#*g#69pbir5cgc7^ovdmqof_-#b42q$d=n687jb5s+1jx%'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'testProj.urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.admindocs',
	'univer',
  
)
