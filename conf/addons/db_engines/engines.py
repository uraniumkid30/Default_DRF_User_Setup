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
    
    @classmethod
    def get_engine_fields(cls, data: dict) -> dict:
        if not data.get("HOST"):
            data["HOST"] = "localhost"
        return super(PostgresqlEngine, cls).get_engine_fields(data)


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
