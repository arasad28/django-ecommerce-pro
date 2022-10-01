

import os

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR,'templates')
STATIC_DIR = os.path.join(BASE_DIR,'static')
MEDIA_DIR = os.path.join(BASE_DIR,'media')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-51o6yf87o@t^+##kv%!c02fs#bbd%q*1dgvx)kssj2ch-l3xlk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #packages
    'crispy_forms',
    'django_summernote',

    #app
    'app_shop',
    'app_login',
    'app_order',
    'app_payment',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'
SUMMERNOTE_THEME = 'bs4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# custom user model 
AUTH_USER_MODEL = 'app_login.User'
ROOT_URLCONF = 'ecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR,],
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

WSGI_APPLICATION = 'ecommerce.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

#stripe
STRIPE_PUBLIC_KEY = "pk_test_51L80ZPKPGYBMzBMKlhUaKKeQ0jjiDpMNiZxF8rhGgXmAdBfEaM6qNsuMtnV1aolTBvZjt9dw3yHhLYnJN3MeUw1000A5WHYx1M"
STRIPE_SECRET_KEY = "sk_test_51L80ZPKPGYBMzBMKFWTNSZgpW0IDJ5L8EuTitnUJHSs673pb2K1mHRXt13iQZvIkV42EWmgUCHeBCj0F8EILZAoG00VnUiglLE"

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Dhaka'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [STATIC_DIR,] 

MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

LOGIN_URL = '/account/login/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
