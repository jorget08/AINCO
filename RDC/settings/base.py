import json
import os
from django.core.exceptions import ImproperlyConfigured

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

with open("secret.json") as f:
    secret = json.loads(f.read())

def get_secret(secret_name, secrets=secret):
    try:
        return secrets[secret_name]
    except:
        msg = "la variable %s no existe" % secret_name
        raise ImproperlyConfigured(msg)




# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_secret('SECRET_KEY')


# Application definition

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.humanize',
)
LOCAL_APPS = (
    'applications.users',
    'applications.gestion',
    'applications.adicional',
    'applications.calificaciones',
    'applications.codeudor',
    'applications.conyugue',
    'applications.credito',
    'applications.deudor',
    'applications.empresa',
    'applications.general',
    'applications.pago',
    'applications.sede',
    'applications.acuerdo',
    'applications.biblioteca',
    'applications.castigados',
    'applications.actaDespacho',
    'applications.gestionAbogado',
    'applications.empresaSocia'
)

THIRD_PARTY_APPS = (
    'import_export',
    'celery',
)

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'RDC.urls'

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

WSGI_APPLICATION = 'RDC.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


#CACHE
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://:p72fc7062f685957afd18fec2960103f1092d492a80e2911f115b07cd2be205fd@ec2-52-200-161-135.compute-1.amazonaws.com:9880",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {
                "ssl_cert_reqs": None
            },
            "PASSWORD": "p72fc7062f685957afd18fec2960103f1092d492a80e2911f115b07cd2be205fd"
        }
    }
}



# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

AUTH_USER_MODEL = 'users.User'

LANGUAGE_CODE = 'es-col'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST = 'smtp-mail.outlook.com'
EMAIL_PORT = 587

CELERY_BROKER_URL = 'redis://:p72fc7062f685957afd18fec2960103f1092d492a80e2911f115b07cd2be205fd@ec2-52-200-161-135.compute-1.amazonaws.com:9880'
REDIS_TLS_URL = 'rediss://:p72fc7062f685957afd18fec2960103f1092d492a80e2911f115b07cd2be205fd@ec2-52-200-161-135.compute-1.amazonaws.com:9880'
CELERY_REDIS_PORT = 9880
CELERY_REDIS_HOST = 'ec2-52-200-161-135.compute-1.amazonaws.com'

