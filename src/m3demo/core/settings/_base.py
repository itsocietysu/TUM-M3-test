# coding: utf-8
import os

from pathlib2 import Path


BASE_DIR = Path(__file__).parents[4].as_posix()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mzk7%q6xmqx#lr$uj7to$jr*+%449p50#ahr)097vka%9bzt!('

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.auth',

    'm3',
    'm3_ext',
    'objectpack',
    'wsfactory',

    'm3demo.core',
    'm3demo.desktop',
    'm3demo.Jedi'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
]

ROOT_URLCONF = 'm3demo.core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': list(set(
            os.path.dirname(path)
            for name in ('educommon', 'm3demo')
            for path in __import__(name).__path__
        )),
        'OPTIONS': {
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'm3_ext.ui.js_template_loader.Loader',
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'm3demo.desktop.context_processors.desktop',
            ],
        },
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'localhost',
        'NAME': 'm3demo',
        'USER': 'm3demo',
        'PASSWORD': 'm3demo',
    }
}

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

#: Префикс URL для доступа к веб-сервисам.
WS_MAIN_PREFIX = 'ws'

#: Путь к файлу конфигурации wsfactory.
WSFACTORY_CONFIG_FILE = Path(BASE_DIR).joinpath(
    'src', 'm3demo', 'wsfactory_config.xml'
).as_posix()
