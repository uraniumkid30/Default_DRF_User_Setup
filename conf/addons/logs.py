import os
from conf.env_manager import env


def get_logs_settings(logs_dir: str = "", installed_apps: list = []) -> str:
    if not env.bool("USE_LOGGERS", True):
        return {}

    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "standard": {
                "format": "[%(asctime)s] %(levelname)s %(message)s - %(pathname)s#lines-%(lineno)s",
                "datefmt": "%d/%b/%Y %H:%M:%S",
            },
        },
        "handlers": {
            "default": {
                "level": "DEBUG",
                "class": "logging.handlers.RotatingFileHandler",
                "filename": os.path.join(logs_dir, "default.log"),
                "formatter": "standard",
                "maxBytes": 104857600,
            },
            "handler_error": {
                "level": "ERROR",
                "class": "logging.FileHandler",
                "filename": os.path.join(logs_dir, "error.log"),
            },
            "SysLog": {
                "level": "ERROR",
                "class": "logging.StreamHandler",
            },
            "daily_error": {
                "level": "ERROR",
                "class": "logging.handlers.TimedRotatingFileHandler",
                "filename": os.path.join(logs_dir, "daily_error.log"),
                "when": "midnight",
                "backupCount": 7,
                "formatter": "standard",
            },
        },
        "loggers": {
            "django": {
                "handlers": ["handler_error", "daily_error"],
                "level": "ERROR",
                "propagate": True,
            },
            "": {
                "handlers": ["default", "daily_error"],
                "level": "INFO",
                "propagate": True,
            },
        },
    }

    MY_LOGGERS = {}
    for app in installed_apps:
        MY_LOGGERS[app] = {
            "handlers": ["SysLog"],
            "level": "INFO",
            "propagate": True,
        }
    LOGGING["loggers"].update(MY_LOGGERS)
    return LOGGING
