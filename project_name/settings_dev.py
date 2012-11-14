# Dev environment (previously local) settings for {{ project_name }} project.

#Debug
DEBUG = True
TEMPLATE_DEBUG = True
LOCAL_SETTINGS = True
IS_LOCAL = True

import dj_database_url
DATABASES = {'default': dj_database_url.config(default='postgres://localhost/{{project_name}}')}

# For designers
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': '{{ project_name }}.db',
#         'USER': '',
#         'PASSWORD': '',
#         'HOST': '',
#         'PORT': ''
#     }
# }


# Make this unique, and don't share it with anybody.
SECRET_KEY = '{{ secret_key }}'

# Show emails in the console during developement.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Prior/Alternate email settings
# EMAIL_HOST = 'localhost'
# EMAIL_PORT = 1025
# EMAIL_HOST_PASSWORD = ''
# EMAIL_HOST_USER = ''
# DEFAULT_FROM_EMAIL = 'webmaster@localhost'
# EMAIL_USE_TLS = False

#Media
MEDIA_URL = '/media/'
STATIC_URL = '/static/'


CACHES = {
  'default': {
    'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    #'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
    'LOCATION': '127.0.0.1:11211',
  }
}