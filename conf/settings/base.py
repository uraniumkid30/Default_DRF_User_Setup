import os
from conf.addons.constants import *
from conf.addons.directories import (
    THEME_DIR,
    LOGS_DIR,
    STATIC_COLLECTION_DIR,
    MEDIA_DIR,
)
from conf.addons.apps import INSTALLED_APPS, LOCAL_APPS
from conf.addons.logs import get_logs_settings

INTERNAL_IPS = ("127.0.0.1",)

LOGIN_URL = "/login/"
LOGOUT_URL = "/logout/"

ANONYMOUS_URLS = [
    r"^admin/$",
    r"^admin/login/$",
    r"^media/",
    r"^static/",
]

# Application definition

ALLOWED_HOSTS = ["*"]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    # "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "conf.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(THEME_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin,
    'applications.accounts.managers.backends.SettingsBackend',
    'django.contrib.auth.backends.ModelBackend',

]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = STATIC_COLLECTION_DIR  # is the folder location of static files when collectstatic is run
MEDIA_URL = "/media/"
MEDIA_ROOT = MEDIA_DIR

# STATICFILES_DIRS = [
#     os.path.join(THEME_DIR, "static"),
# ] # tells Django where to look for static files in a Django project, such as a top-level static folder

# DJANGO_STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"
# WHITENOISE_STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

LOGGING = get_logs_settings(LOGS_DIR, LOCAL_APPS)
AUTH_USER_MODEL = 'accounts.User'
