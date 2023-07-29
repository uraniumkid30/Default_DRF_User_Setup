import os
from pathlib import Path

from conf.env_manager import env
from services.file_manager.utils import FileProcessingTool

# Build paths inside the project like this: BASE_DIR / 'subdir'.
SETTINGS_DIR = Path(__file__).resolve().parent  # settings dir
PROJECT_DIR = Path(__file__).resolve().parent.parent  # project conf dir
ROOT_DIR = Path(__file__).resolve().parent.parent.parent  # dir housing conf dir
BASE_DIR = ROOT_DIR

DATABASE_DIR = os.path.join(PROJECT_DIR, "databases")
REQUIREMENTS_DIR = os.path.join(ROOT_DIR, "requirements")
MISCELLANEOUS_DIR = os.path.join(PROJECT_DIR, "miscellaneous")
LOGS_DIR = os.path.join(MISCELLANEOUS_DIR, "LOGS")
FILES_DIR = os.path.join(MISCELLANEOUS_DIR, "FILES")
THEME_DIR = os.path.join(MISCELLANEOUS_DIR, "THEMES")

ARCHIVE_DIR = os.path.join(FILES_DIR, "ARCHIVE")
NEWFILES_DIR = os.path.join(FILES_DIR, "NEW_FILES")
TEMPLATES_DIR = os.path.join(THEME_DIR, "templates")
STATIC_DIR = os.path.join(THEME_DIR, "static")
MEDIA_DIR = os.path.join(THEME_DIR, "media")
STATIC_COLLECTION_DIR = os.path.join(THEME_DIR, "static_collection")


def is_folder_exists(_dir: str) -> bool:
    if os.path.exists(_dir) and os.path.isdir(_dir):
        return True
    return False


def check_and_create_dir(dir_name: str, retrn_val: str = False):
    not_exists: bool = not is_folder_exists(dir_name)
    if not_exists:
        os.makedirs(dir_name)

    if retrn_val:
        return not_exists


def create_neccessary_directories():
    directory_list = [
        DATABASE_DIR,
        MISCELLANEOUS_DIR,
        REQUIREMENTS_DIR,
        THEME_DIR,
        FILES_DIR,
        LOGS_DIR,
        STATIC_DIR,
        MEDIA_DIR,
        STATIC_COLLECTION_DIR,
        TEMPLATES_DIR,
        ARCHIVE_DIR,
        NEWFILES_DIR,
        os.path.join(STATIC_DIR, "css"),
        os.path.join(STATIC_DIR, "js"),
        os.path.join(STATIC_DIR, "images"),
    ]
    for _dir in directory_list:
        FileProcessingTool.check_and_create_dir(_dir)


if env.bool("CREATE_DEFAULT_DIRECTORIES", True):
    create_neccessary_directories()
else:
    LOGS_DIR = ""
    THEME_DIR = ""
    TEMPLATES_DIR = ""
    REQUIREMENTS_DIR = ""
    STATIC_DIR = "/vol/web/static/"
    MEDIA_DIR = "/vol/web/media/"
    STATIC_COLLECTION_DIR = ""
