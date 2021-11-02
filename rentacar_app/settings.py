import os
from decouple import config
import dj_database_url
import django_heroku


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = config("SECRET_KEY")
DEBUG = True
ALLOWED_HOSTS = ['rentacar-heroku.herokuapp.com']

INSTALLED_APPS = [
    'user_account',
    'homepage',
    'cars',
    'user_contact',
    'facilities',
    'sendgrid',
    'django_filters',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
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
]

ROOT_URLCONF = 'rentacar_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'rentacar_app.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config("DATABASE_NAME"),
        'USER': config("DATABASE_USER"),
        'PASSWORD': config("DATABASE_PASSWORD"),
        'HOST': config("DATABASE_HOST"),
        'PORT': config("DATABASE_PORT"),

    }
}

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

# LOGIN_REDIRECT_URL = 'home'
# LOGOUT_REDIRECT_URL = 'home'

# LOGIN_REDIRECT_URL = '/'
# LOGOUT_REDIRECT_URL = '/'

AUTH_USER_MODEL = "user_account.Account"

AUTHENTICATION_BACKENDS = {
    'django.contrib.auth.backends.ModelBackend'
}

LANGUAGE_CODE = 'pl'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

PROJECT_ROOT = os.path.join(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
BASE_URL = "home"

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_TEMPLATE_PACK = "bootstrap4"

SENDGRID_SANDBOX_MODE_IN_DEBUG = False
EMAIL_BACKEND = config("EMAIL_BACKEND")
SENDGRID_API_KEY = config("SENDGRID_API_KEY")
DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL")

prod_db = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)

django_heroku.settings(locals())
