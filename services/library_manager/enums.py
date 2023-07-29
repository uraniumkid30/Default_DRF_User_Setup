from dataclasses import dataclass, asdict
from conf.core.base_dataclasses import DefaultSchema


@dataclass(frozen=True)
class LibraryManagerConfigurationSchema(DefaultSchema):
    # List = field(default_factory=lambda: ["loyalty"])
    pipfile_path: str = "pipfile.lock"
    base_path: str = "requirements/base.txt"
    development_path: str = "requirements/development.txt"


@dataclass(frozen=True)
class LibraryManagers(DefaultSchema):
    PIP: str = "PIP"
    PIPENV: str = "PIPENV"
