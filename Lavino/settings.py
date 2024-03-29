"""
Django settings for Lavino project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
from .other_settings import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# This  part of code is for keep secret variables secure and also it to change some parameters for Development/Production
# It returns the secrets_dict which can be used in the main code
# This file is different in Server and my local PC
secret_file = 'LavinoKEYS.txt'
secrets = ['SECRET_KEY', 'DEBUG' , 'DATABASE_NAME', 'DATABASE_USERNAME', 'DATABASE_PASSWORD',
 'EMAIL_HOST', 'EMAIL_HOST_USER', 'EMAIL_HOST_PASSWORD', 'RECAPTCHA_PUBLIC_KEY', 'RECAPTCHA_PRIVATE_KEY']
SECRETS_DIR = BASE_DIR
filepath = os.path.join(SECRETS_DIR, secret_file)
secrets_dict = {}
with open(filepath) as fp:
   line = fp.readline()
   for item in secrets:
       secrets_dict[item] = line.strip()
       line = fp.readline()


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secrets_dict['SECRET_KEY']

# ReCaptcha Google Keys
RECAPTCHA_PUBLIC_KEY = secrets_dict['RECAPTCHA_PUBLIC_KEY']
RECAPTCHA_PRIVATE_KEY = secrets_dict['RECAPTCHA_PRIVATE_KEY']


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(secrets_dict['DEBUG'])

ALLOWED_HOSTS = ['localhost',
                 '127.0.0.1',
                 '161.35.102.245',
                 'www.lavinomood.com',
                 'lavinomood.com',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',

    # My APPs
    'apps.baseApp',
    'apps.blogApp',

    # for models phone number field
    'phonenumber_field',

    # Captcha
    'captcha',

    # Robot.txt
    'robots',

    # for models Text editor
    'ckeditor',
    'ckeditor_uploader',
]

MIDDLEWARE = [
    # Gzip Compression
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Lavino.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR,],
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

WSGI_APPLICATION = 'Lavino.wsgi.application'

# Email settings
EMAIL_HOST = secrets_dict['EMAIL_HOST']
EMAIL_PORT = 465
EMAIL_HOST_USER = secrets_dict['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = secrets_dict['EMAIL_HOST_PASSWORD']
EMAIL_USE_SSL = True

# Digital Ocean Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': secrets_dict['DATABASE_NAME'],
        'USER': secrets_dict['DATABASE_USERNAME'],
        'PASSWORD': secrets_dict['DATABASE_PASSWORD'],
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

SITE_ID = 1

# Robots.txt setup
ROBOTS_SITEMAP_URLS = [
    'https://www.lavinomood.com/LavinoMap.xml',
]
ROBOTS_USE_SCHEME_IN_HOST = True
ROBOTS_USE_HOST = False


DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en'
LANGUAGES = [
    ('en', 'English'),
    ('tr', 'Turkish'),
    ('fa', 'Persian'),
]


TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# This setting is for scss files
# STATICFILES_FINDERS = ['django.contrib.staticfiles.finders.FileSystemFinder',
#                         'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#                         # other finders
#                         'compressor.finders.CompressorFinder',]
# COMPRESS_PRECOMPILERS = (
#     ('text/x-scss', 'django_libsass.SassCompiler'),
# )
# COMPRESS_OFFLINE = True
# LIBSASS_OUTPUT_STYLE = 'compressed'

STATIC_URL = '/static/'

# The root for collecting all static files
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

# This is for production use only.
# https://docs.djangoproject.com/en/1.10/ref/contrib/staticfiles/#manifeststaticfilesstorage
if DEBUG == False:
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

# The root for uploaded files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# DEBUG_PROPAGATE_EXCEPTIONS = False
