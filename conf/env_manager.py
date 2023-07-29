import os

import environ
from django.core.exceptions import ImproperlyConfigured

env = environ.Env()


def env_to_enum(enum_cls, value):
    for x in enum_cls:
        if x.value == value:
            return x

    raise ImproperlyConfigured(
        f"Env value {repr(value)} could not be found in {repr(enum_cls)}"
    )


def get_env_variable(var_name, default=None, strict_mode=False):
    """Get the environment variable or return exception."""
    if not strict_mode:
        return os.environ.get(var_name, default)
    try:
        return os.environ[var_name]
    except KeyError as error:
        error_msg = f"Set the {var_name} environment variable {error}"
        raise ImproperlyConfigured(error_msg)
