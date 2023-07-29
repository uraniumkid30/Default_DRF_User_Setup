from .engines import SqliteEngine, PostgresqlEngine
from .enums import EngineNames


def db_engine_factory(data: dict = {}, engine_name: str = EngineNames.sqlite):
    engine = SqliteEngine
    if engine_name == EngineNames.postgres:
        engine = PostgresqlEngine
    return engine.get_engine_fields(data)
