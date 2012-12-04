# Global settings for {{ project_name }} project.
import os
import sys

PROJECT_PATH_INNER = os.path.dirname(__file__)
PROJECT_PATH = os.path.dirname(PROJECT_PATH_INNER)
APPLIB_DIR = os.path.join(PROJECT_PATH, "applib")

if APPLIB_DIR not in sys.path[:2]:
  sys.path.insert(1, APPLIB_DIR)

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

#DATABASE IN BOTTOM ENVIRONMENT CONFIG AREA


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'assets/media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_PATH, 'assets/static-destination')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_PATH, 'assets/static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',    
)

ROOT_URLCONF = '{{ project_name }}.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = '{{ project_name }}.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_PATH, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    
    '{{ project_name }}.misc.context_processors.date_formats',
    '{{ project_name }}.misc.context_processors.is_local',
    
    #AllAuth
    'allauth.account.context_processors.account',
    'allauth.socialaccount.context_processors.socialaccount',    
)

FIXTURE_DIRS = (
    os.path.join(PROJECT_PATH, 'fixtures'),
)

MESSAGE_STORAGE = 'django.contrib.messages.storage.fallback.FallbackStorage'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    
    #system/pip installed 3rd party apps
    'south',
    'gunicorn',
    'storages',
    's3_folder_storage',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    #'allauth.socialaccount.providers.facebook',
    #'allauth.socialaccount.providers.twitter',
    
    #applib installed 3rd party apps
    
    #Project apps - utility
    '{{ project_name }}.misc',      #gets views and urls, incl basic homepage
    '{{ project_name }}.templates', #gets template tags
    
    #Project apps - core
    
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

#TODO update IS_LOCAL
#make something like "SERVE_ALL_LOCALLY"

# NO DJANGO_ENV FALLBACK
# Environment variables are mostly not given fallbacks on purpose
# Better to fail early and informatively than to initially appear to work and later fail obscurely
assert 'DJANGO_ENV' in os.environ, 'Set DJANGO_ENV environment variable!'
DJANGO_ENV = os.environ['DJANGO_ENV']

if DJANGO_ENV not in ["PRODUCTION", "TEST", "DEV"]:
  raise EnvironmentError("DJANGO_ENV set to '%s'.  Configured environments are 'PRODUCTION', 'TEST', 'DEV'" % DJANGO_ENV)

####################################### 
#PRODUCTION ENVIRONMENT
####################################### 
if DJANGO_ENV == "PRODUCTION":
  #BEHAVIOR FLAGS
  # To make it easier to turn DEBUG on and off
  # heroku config:add DJANGO_DEBUG=True
  # heroku config:remove DJANGO_DEBUG
  DEBUG = bool(os.environ.get('DJANGO_DEBUG', False))
  TEMPLATE_DEBUG = DEBUG
  IS_LOCAL = False

  #DATABASE
  import dj_database_url  
  DATABASES = {'default': dj_database_url.config(default='postgres://localhost/{{ project_name }}')}  
  
  #EMAIL
  EMAIL_HOST= 'smtp.sendgrid.net'
  EMAIL_HOST_USER = os.environ['SENDGRID_USERNAME']
  EMAIL_HOST_PASSWORD = os.environ['SENDGRID_PASSWORD']
  EMAIL_PORT = 587
  EMAIL_USE_TLS = True

  #AWS KEYS
  AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
  AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
  AWS_STORAGE_BUCKET_NAME = '{{project_name}}-assets-production'

  #ASSETS: STATIC FILES, MEDIA
  DEFAULT_FILE_STORAGE = 's3_folder_storage.s3.DefaultStorage'
  STATICFILES_STORAGE = 's3_folder_storage.s3.StaticStorage'
  DEFAULT_S3_PATH = "media"
  STATIC_S3_PATH = "static"

  MEDIA_ROOT = '/%s/' % DEFAULT_S3_PATH
  STATIC_ROOT = "/%s/" % STATIC_S3_PATH
  MEDIA_URL = 'http://%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
  STATIC_URL = 'http://%s.s3.amazonaws.com/static/' % AWS_STORAGE_BUCKET_NAME
  ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
  
  #CACHES
  # TODO add memcached/redis defaults
  
  #QUEUES
  # TODO add celery defaults
  
  #MONITORING
  # TODO add newrelic defaults

 
####################################### 
# TESTING ENVIRONMENT  
#######################################
elif DJANGO_ENV == "TEST":
  # Not set up by default
  # should be exact settings as production with different servers/databases
  raise NotImplementedError("TEST environment settings have not been set up")

  
  
#######################################   
# DEV / LOCAL ENVIRONMENT  
####################################### 
elif DJANGO_ENV == "DEV":
  #BEHAVIOR FLAGS
  # To make it easier to turn DEBUG on and off
  DEBUG = bool(os.environ.get('DJANGO_DEBUG', True))
  TEMPLATE_DEBUG = DEBUG
  IS_LOCAL = True  
  
  #DATABASE
  import dj_database_url
  DATABASES = {'default': dj_database_url.config(default='postgres://localhost/{{project_name}}')}
  # Alt database settings
  # DATABASES = {
  #   'default': {
  #     'ENGINE': 'django.db.backends.sqlite3',
  #     'NAME': '{{ project_name }}.db',
  #     'USER': '',
  #     'PASSWORD': '',
  #     'HOST': '',
  #     'PORT': '',
  #   }
  # }
    
  #EMAIL
  EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

  #ASSETS: STATIC FILES, MEDIA
  MEDIA_URL = '/media/'
  STATIC_URL = '/static/'  

  #CACHES
  # Todo add memcached/redis defaults
  # CACHES = {
  #   'default': {
  #     'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
  #     #'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
  #     'LOCATION': '127.0.0.1:11211',
  #   }
  # }    
  
  #QUEUES
  # TODO add celery defaults
  
  #MONITORING
  # TODO add newrelic/monitoring  https://newrelic.com/docs/python/django-on-heroku-quick-start
  
  
  #ENVIRONMENT SPECIFIC 
  INSTALLED_APPS += (
    'debug_toolbar',
  )

  MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
  )
  
  

  # LOCAL SETTINGS
  # Tolerate local settings in DEV environment 
  try:
      LOCAL_SETTINGS
  except NameError:
      try:
          from local_settings import *
      except ImportError:
          pass

