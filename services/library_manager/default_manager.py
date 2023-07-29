from .base import (
    AbstractLibraryManager,
)


class DefaultLibraryManager(AbstractLibraryManager):
    def __init__(self, configuration: dict = {}):
        AbstractLibraryManager.__init__(self, configuration)

    def get_configuration(self, configuration):
        pass

    def update_requirements(self):
        pass
