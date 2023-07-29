import functools


DEFAULT_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
LOCAL_APPS = [
    "applications.accounts",
]

THIRD_PARTY_APPS = [
    # "rest_framework",
    # "whitenoise.runserver_nostatic",
]

ALL_APPS_CONTAINER = {
    "DEFAULT_APPS": DEFAULT_APPS,
    "LOCAL_APPS": LOCAL_APPS,
    "THIRD_PARTY_APPS": THIRD_PARTY_APPS,
}

# Application definition
INSTALLED_APPS: list = functools.reduce(lambda x, y: x + y, ALL_APPS_CONTAINER.values())
