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
from conf.addons.db_engines import db_engine_factory

db_name = "production_database.sqlite3"
db_path = os.path.join(DATABASE_DIR, db_name)
FileProcessingTool.check_and_create_file(db_path)
DATABASES = {
    "default": db_engine_factory(
        data={"NAME": db_path},
        engine_name=env.str("DATABASE_ENGINE", "sqlite"),
    )
}

DEBUG = env.bool("DJANGO_DEBUG_SETTINGS", False)

SECRET_KEY = f"django-insecure-{secrets.token_urlsafe(50)}"

base_requirements = os.path.join(REQUIREMENTS_DIR, "base.txt")
prod_requirements = os.path.join(REQUIREMENTS_DIR, "production.txt")
if not FileProcessingTool.is_file_exists(base_requirements):
    subprocess.call(f"pip freeze > {base_requirements}", shell=True)

if not FileProcessingTool.is_file_exists(prod_requirements):
    try:
        with open(prod_requirements, "w") as f:
            f.write("-r base.txt")
    except Exception as err:
        print(f"Error: {err}")
