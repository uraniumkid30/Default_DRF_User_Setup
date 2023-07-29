from typing import NoReturn
from abc import ABC, abstractmethod

from .enums import LibraryManagerConfigurationSchema


class AbstractLibraryManager(ABC):
    """Interface for all solid implementations"""

    def __init__(self, configuration: dict = {}):
        self.config: LibraryManagerConfigurationSchema = (
            self.get_configuration(configuration)
        )

    @abstractmethod
    def update_requirements(
        self,
    ) -> NoReturn:
        """Updates requirements"""
        pass

    @abstractmethod
    def get_configuration(self, configuration: dict) -> LibraryManagerConfigurationSchema:
        """Creates a Configuration"""
        if configuration:
            return LibraryManagerConfigurationSchema(configuration)
        return LibraryManagerConfigurationSchema()

    @classmethod
    def clean_requrements_for_production(cls):
        """for new version of pip to avoid conflict"""
        # re_pattern: str = "==\w+.+.+"
        dump_data: list = []
        with open("requirements/base.txt") as package_file:
            packages = package_file.read()
            packages = packages.splitlines()
            for package in packages:
                dump_data.append(package.split("==")[0])
        with open("requirements/base.txt", "w") as package_file:
            for package in dump_data:
                package_file.write(f"{package}\n")
