"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import dj_database_url
import cloudinary
import cloudinary.api
import cloudinary.uploader

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5hv)3q_18$d4_9($ek&(ggv#6f$x+x$3h0^rn=ppx!f&%%&*fv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com', 'www.evanlarrimore.com']

# Force HTTPS for cookies and sessions
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Ensure browser only sends cookies over HTTPS
SECURE_BROWSER_XSS_FILTER = True

# Prevent content sniffing (security against MIME-type attacks)
SECURE_CONTENT_TYPE_NOSNIFF = True

# Enable HSTS (HTTP Strict Transport Security) for HTTPS enforcement
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Ensure cookies are not accessible via JavaScript (for security)
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True

# X-Frame-Options header to prevent clickjacking attacks
X_FRAME_OPTIONS = 'DENY'    


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog.apps.BlogConfig',
    'django_filters',
    'cloudinary'
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Redirect HTTP traffic to HTTPS (if you're using SSL)
if os.getenv('DJANGO_ENV') == 'production':
    # Production-specific settings
    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_SECONDS = 31536000  # Enable HSTS only in production

else:
    # Local development settings
    SECURE_SSL_REDIRECT = False  # Disable SSL redirection for local development

# Redirect example.com to www.example.com
if os.getenv('DJANGO_ENV') == 'production':

    PREPEND_WWW = True

    ROOT_URLCONF = 'mysite.urls'
else:
    # Local development settings (default)
    PREPEND_WWW = False  # You likely don't want this in local development
    ROOT_URLCONF = 'mysite.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'blog',
        'USER': 'elarrimore',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}

DATABASE_URL = os.getenv('DATABASE_URL')

if DATABASE_URL:
    db_from_env = dj_database_url.config(conn_max_age=500)
    DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators




AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')




# media config
MEDIA_URL = '/media/'
MEDIA_ROOT = 'os.path.join(BASE_DIR, media)'


# cloudinary config
cloudinary.config(
   cloud_name = 'dl3h6iib2',
   api_key = '975132373835258',
   api_secret = '8hW3R3U4n-fj9msb3F_um8EPF2s'
)




STATICFILES_STORAGE = {
    "statfiles":{
        "BACKEND":
'whitenoise.storage.CompressedManifestStaticFilesStorage',
    },

}


DEFAULT_AUTO_FIELD='django.db.models.AutoField' 

#LOGGING = {
#    'version': 1,
#    'disable_existing_loggers': False,
#    'handlers': {
#        'console': {
#            'class': 'logging.StreamHandler',
#        },
#    },
#    'loggers': {
#        'django': {
#            'handlers': ['console'],
#             'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
#        },
#    },
#}
