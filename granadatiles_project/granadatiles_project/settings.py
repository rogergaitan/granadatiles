﻿"""
Django settings for granadatiles_project project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q++cnv!u1oy_at*@5f*y3z8=xw2=ecs(y-73*xjhncg4f^fb!3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #third party apps
    'django_summernote',
    'sorl.thumbnail',
    'rest_framework',
    'rest_framework.authtoken',
    'social.apps.django_app.default',
    'kombu.transport.django',

    #project apps
    'apps.customadmin',
    'apps.news',
    'apps.galleries',
    'apps.content',
    'apps.tiles',

]

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
]

ROOT_URLCONF = 'granadatiles_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'granadatiles_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

from django.utils.translation import ugettext_lazy as _
LANGUAGES = (
  ('en', _('English')),
  ('es', _('Spanish')),
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'templates', 'locale'),
    os.path.join(BASE_DIR, 'granadatiles_project', 'locale'),
    )

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATIC_URL = '/static/'
IMAGES_URL = STATIC_URL
if not DEBUG:
    IMAGES_URL = STATIC_URL + 'build/'

STATIC_ROOT = os.path.join(ROOT_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(ROOT_DIR, 'media')

THUMBNAIL_BACKEND = 'core.extensions.SEOThumbnailBackend'
THUMBNAIL_PREFIX = 'images/'

DAB_FIELD_RENDERER = 'django_admin_bootstrapped.renderers.BootstrapFieldRenderer'

from django.contrib import messages

MESSAGE_TAGS = {
            messages.SUCCESS: 'alert-success success',
            messages.WARNING: 'alert-warning warning',
            messages.ERROR: 'alert-danger error'
}


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    )
}

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.google.GoogleOpenId',
    'social.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_URL_NAMESPACE = 'social'

SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'email']

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
  #'locale': 'ru_RU',
  'fields': 'id, name, email'
}

SOCIAL_AUTH_FACEBOOK_KEY = '1653932784823559'
SOCIAL_AUTH_FACEBOOK_SECRET = '4d0e4c10fee651e388b74bcf68a6ced2'

BROKER_URL = 'django://'
