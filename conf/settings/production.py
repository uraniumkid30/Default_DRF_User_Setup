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
data = {"NAME": db_path}
pg_data = {
    "NAME": os.environ.get("DB_NAME"),
    "USER": os.environ.get("DB_USER"),
    "PASSWORD": os.environ.get("DB_PASSWORD"),
    "HOST": os.environ.get("DB_HOST"),
}
res = db_engine_factory(
    data=pg_data,
    engine_name=env.str("DATABASE_ENGINE", "sqlite"),
)
DATABASES = {
    "default": res
}

DEBUG = env.bool("DJANGO_DEBUG_SETTINGS", False)

SECRET_KEY = env.str("SECRET_KEY")
ENVIRONMENT = env.str("DJANGO_SETTINGS_MODULE", ".PRODUCTION").split(".")[-1].upper()
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
