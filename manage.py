#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from services.library_manager import lib_manager_factory


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conf.settings.production")
    try:
        from django.core.management import execute_from_command_line
        lib_manager = lib_manager_factory()
        lib_manager.update_requirements()
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
