import os

import environs

env = environs.Env()
env.read_env()

DATABASES = {
    'default': {
        'ENGINE': env.str('PG_ENGINE'),
        'HOST': env.str('PG_HOST'),
        'PORT': env.str('PG_PORT'),
        'NAME': env.str('PG_NAME'),
        'USER': env.str('PG_USER1'),
        'PASSWORD': env.str('PG_PASSWORD'),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = env.str('SECRET_KEY')

DEBUG = env.bool('DEBUG', False)

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
