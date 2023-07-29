from .base import (
    AbstractLibraryManager,
)
import pkg_resources


class PipLibraryManager(AbstractLibraryManager):
    def __init__(self, configuration: dict = {}):
        AbstractLibraryManager.__init__(self, configuration)

    def get_configuration(self, configuration):
        return AbstractLibraryManager.get_configuration(self, configuration)

    def update_requirements(self):
        list_of_packages: list = [tuple(str(ws).split()) for ws in pkg_resources.working_set]
        all_packages: dict = dict(sorted(list_of_packages, key=lambda x: (x[0].lower(), x)))
        packages_available: list = []
        try:
            with open(self.config.base_path, "r") as package_file:
                for _package in package_file:
                    packages_available.append(_package.replace("\n", ""))

            if len(all_packages.items()) > len(packages_available):
                with open(self.config.base_path, "w") as package_file:
                    for _package, _version in all_packages.items():
                        package_file.write(f"{_package}\n")
                with open(self.config.development_path, "w") as package_file:
                    for _package, _version in all_packages.items():
                        package_file.write(f"{_package}=={_version}\n")
        except FileNotFoundError as err:
            print(f"Error {err}")
