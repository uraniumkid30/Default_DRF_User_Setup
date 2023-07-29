import json

from .base import (
    AbstractLibraryManager,
)


class PipenvLibraryManager(AbstractLibraryManager):
    def __init__(self, configuration: dict = {}):
        AbstractLibraryManager.__init__(self, configuration)

    def get_configuration(self, configuration):
        return AbstractLibraryManager.get_configuration(self, configuration)

    @classmethod
    def read_json_file(cls, path: str) -> dict:
        with open(path) as f:
            return json.load(f)

    @classmethod
    def write_to_text_file(cls, path: str, data: str, mode: str = "a+"):
        with open(path, mode) as f:
            f.write(data)

    def update_requirements(self):
        root = self.read_json_file(self.config.pipfile_path)
        root_info: tuple = root["default"].items()
        self.write_to_text_file(self.config.development_path, "", "w")
        self.write_to_text_file(self.config.base_path, "", "w")
        for counter, info in enumerate(root_info, 1):
            name, pkg = info
            version = pkg["version"]
            seperator = "\n" if counter != len(root_info) else ""
            data = f'{name}{version}{seperator}'
            self.write_to_text_file(self.config.development_path, data)
            self.write_to_text_file(self.config.base_path, f"{name}{seperator}")
