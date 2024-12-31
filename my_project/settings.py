"""
Django settings for my_project project.

Generated by 'django-admin startproject' using Django 5.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_@%tubbu8f$-j!xqjo6$w=or$bx7%ox!+-*1g)872ihmim4ezl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", "False") == True

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "bodegalmm24.onrender.com,127.0.0.1").split(",")


import dj_database_url 
import os
from dotenv import load_dotenv

#cargar las variables desce el archivo .env
load_dotenv()


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap5',
    'dispositivo',
    'producto',
    'crispy_forms', 
    "crispy_bootstrap5",
    "storages",
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5" 
CRISPY_TEMPLATE_PACK = "bootstrap5"

# Configuración de AWS S3
AWS_ACCESS_KEY_ID = 'KEY_ID'
AWS_SECRET_ACCESS_KEY = 'SECRET_KEY'
AWS_STORAGE_BUCKET_NAME = 'gestionbodegalmm'
AWS_S3_REGION_NAME = 'us-east-2'  # Ejemplo: 'us-west-1'
AWS_QUERYSTRING_AUTH = False  # Opcional: hace que las URL sean públicas


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'my_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'my_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.parse(
        'postgresql://bodega24_user:SeaXwK7W0Oz4N7ubuOdj0903uMVi7Fqm@dpg-ctplkua3esus73dj27g0-a.oregon-postgres.render.com:5432/bodega24'
    ),
    'local': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'm7dia3',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5433',
    }
}




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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = '/dispositivo/templates/registration/login/'
LOGIN_REDIRECT_URL = '/'  # Redirige después de iniciar sesión

# settings.py
TIME_ZONE = 'America/Santiago'

USE_TZ = True  # Si quieres manejar zonas horarias con soporte UTC

# Configuración para los archivos cargados
MEDIA_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.us-west-2.amazonaws.com/media/'  # URL pública para acceder a los archivos
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Ruta absoluta a la carpeta 'media' en el directorio del proyecto

