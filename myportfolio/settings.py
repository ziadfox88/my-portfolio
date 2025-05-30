"""
Django settings for myportfolio project.

Generated by 'django-admin startproject' using Django 5.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv
# import cloudinary
# import cloudinary.uploader
# from cloudinary.utils import cloudinary_url
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


load_dotenv()
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost','127.0.0.1','my-portfolio-rjrx.vercel.app']
CSRF_TRUSTED_ORIGINS = ['http://127.0.0.1/','https://my-portfolio-rjrx.vercel.app/']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "whitenoise.runserver_nostatic",
    # 'cloudinary_storage',
    # 'cloudinary',
    'portfolio',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = 'myportfolio.urls'

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

WSGI_APPLICATION = 'myportfolio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.getenv('NAME'),
#         'USER': os.getenv('USER'),
#         'PASSWORD': os.getenv('DB_PASSWORD_Z'),
#         'HOST': os.getenv('HOST'),
#         'OPTIONS': {'sslmode': 'require'},
#     }
# }
# 'PASSWORD': os.environ.get['DB_PASSWORD_Z'],

# DATABASES = {
#     'default': {
#         'ENGINE':'django.db.backends.postgresql',
#         # 'NAME':'test1',
#         # 'USER':'ziad',
#         'NAME':'railway',
#         'USER':'postgres',
#         'PASSWORD': os.getenv('DB_PASSWORD_Z'),
#         'HOST':'switchback.proxy.rlwy.net',
#         'PORT':'23007'
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Cairo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'



MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


STATICFILES_DIRS = [
    BASE_DIR / 'static'
]


#white noise static stuff
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# CLOUDINARY_STORAGE = {
#     'CLOUD_NAME': os.getenv('CLOUD_NAME'),
#     'API_KEY': os.getenv('API_KEY'),
#     'API_SECRET': os.getenv('API_SECRET'),
# }
# DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# cloudinary.config(
#     cloud_name=os.getenv('CLOUD_NAME'),
#     api_key=os.getenv('API_KEY'),
#     api_secret=os.getenv('API_SECRET')
# )




# STORAGES = {
#     # ...
#     "staticfiles": {
#         "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
#     },
# }
# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#sending emails 
# settings.py


# Email configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Gmail SMTP server
EMAIL_PORT = 587  # TLS port for Gmail
EMAIL_USE_TLS = True  # Use TLS for secure connection
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')  # Your Gmail address
EMAIL_HOST_PASSWORD = os.getenv('GOOGLE_APP_PASS')  # Password stored in environment variable
DEFAULT_FROM_EMAIL = os.getenv('EMAIL_HOST_USER')  # Sender email
CONTACT_EMAIL =  os.getenv('CONTACT_EMAIL')   # Recipient email (e.g., for contact form submissions)
