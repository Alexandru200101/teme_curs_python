# testare/settings.py

import os
from pathlib import Path

# BASE_DIR: directorul rădăcină al proiectului (conține manage.py)
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-t47nz)r3x1%u&uof#c*n8l82t#$&idn*tkx79#rb9h+3+$&k&g'

DEBUG = True

ALLOWED_HOSTS = []

# Aplicații
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',  # aplicația ta
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'testare.urls'

# URL pe care Django redirecționează utilizatorii neautentificați
LOGIN_URL = '/login-firma/'

# Configurarea template-urilor
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # dacă vrei foldere adiționale, le adaugi aici
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.csrf',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'testare.wsgi.application'

# Configurare bază de date (MySQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'decorsoft',
        'USER': 'root',
        'PASSWORD': 'Lamborghini_01',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

# Validatori parolă
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# Localizare
LANGUAGE_CODE = 'ro-RO'
TIME_ZONE = 'Europe/Bucharest'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Fișiere statice
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',     # proiectul tău: testare/static/
]
# La producție, folosind collectstatic:
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Câmpul implicit pentru chei primare auto
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



