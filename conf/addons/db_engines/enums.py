from conf.core.base_dataclasses import BaseSchema
from dataclasses import dataclass, field


@dataclass(frozen=True)
class EngineNames:
    sqlite: str = 'sqlite'
    postgres: str = 'postgres'


@dataclass(frozen=True)
class BaseEngineSchema(BaseSchema):
    ENGINE: str
    NAME: str


@dataclass(frozen=True)
class ProductionDBSchema(BaseEngineSchema):
    HOST: str = field(default="127.0.0.1", init=False)
    USER: str
    PASSWORD: str
    PORT: str


@dataclass(frozen=True)
class SqliteSchema(BaseEngineSchema):
    ENGINE: str = field(default="django.db.backends.sqlite3", init=False)


@dataclass(frozen=True)
class PostgresqlSchema(ProductionDBSchema):
    ENGINE: str = field(default="django.db.backends.postgresql", init=False)
    PORT: str = field(default="5432", init=False)


@dataclass(frozen=True)
class MysqlSchema(ProductionDBSchema):
    ENGINE: str = field(default="django.db.backends.mysql", init=False)
    PORT: str = field(default="3306", init=False)


@dataclass(frozen=True)
class OracleSchema(ProductionDBSchema):
    ENGINE: str = field(default="django.db.backends.oracle", init=False)
    PORT: str = field(default="1521", init=False)
