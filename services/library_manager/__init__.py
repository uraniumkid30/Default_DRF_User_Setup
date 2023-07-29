import os

from .enums import LibraryManagers
from .pip_manager import PipLibraryManager
from .pipenv_manager import PipenvLibraryManager
from .default_manager import DefaultLibraryManager


def lib_manager_factory(lib_manager: str = ""):
    lib_manager = lib_manager.upper()
    UPDATE_REQUIREMENTS = os.environ.get("UPDATE_REQUIREMENTS", False)
    if not lib_manager or not LibraryManagers.in_choices(lib_manager):
        LIBRARY_MANAGER: str = os.environ.get(
            'LIBRARY_MANAGER',
            LibraryManagers.PIPENV
        )
    else:
        LIBRARY_MANAGER: str = lib_manager
    if not UPDATE_REQUIREMENTS:
        return DefaultLibraryManager()
    if LIBRARY_MANAGER == LibraryManagers.PIP:
        return PipLibraryManager()
    elif LIBRARY_MANAGER == LibraryManagers.PIPENV:
        return PipenvLibraryManager()
    
