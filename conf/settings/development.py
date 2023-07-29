import os
import secrets
import subprocess

from .base import *
from conf.addons.directories import (
    REQUIREMENTS_DIR,
    DATABASE_DIR,
    FileProcessingTool
)
from conf.env_manager import env

db_name = "development_database.sqlite3"
db_path = os.path.join(DATABASE_DIR, db_name)
FileProcessingTool.check_and_create_file(db_path)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": db_path,
    }
}

DEBUG = DEBUG = env.bool("DJANGO_DEBUG_SETTINGS", True)

SECRET_KEY = f"django-insecure-{secrets.token_urlsafe(50)}"

# process requirements
base_requirements = os.path.join(REQUIREMENTS_DIR, "base.txt")
dev_requirements = os.path.join(REQUIREMENTS_DIR, "development.txt")
for _file in [base_requirements, dev_requirements]:
    if not FileProcessingTool.is_file_exists(_file):
        subprocess.call(f"pip freeze > {_file}", shell=True)
