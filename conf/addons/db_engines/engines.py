from .base import BaseEngine
from .enums import (
    SqliteSchema,
    PostgresqlSchema,
    MysqlSchema,
    OracleSchema,
)

from conf.core.types import DataclassEnum


class SqliteEngine(BaseEngine):
    @classmethod
    def get_schema(cls) -> DataclassEnum:
        """ Schema for Sqlite database"""
        return SqliteSchema


class PostgresqlEngine(BaseEngine):
    @classmethod
    def get_schema(cls) -> DataclassEnum:
        """ Schema for Postgres database"""
        return PostgresqlSchema


class MysqlEngine(BaseEngine):
    @classmethod
    def get_schema(cls) -> DataclassEnum:
        """ Schema for Mysql database"""
        return MysqlSchema


class OracleEngine(BaseEngine):
    @classmethod
    def get_schema(cls) -> DataclassEnum:
        """ Schema for Oracle database """
        return OracleSchema
