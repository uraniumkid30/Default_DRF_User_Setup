from dataclasses import dataclass
from abc import ABC, abstractmethod


class BaseEngine(ABC):
    @classmethod
    @abstractmethod
    def get_schema(cls) -> dataclass:
        """ """
        pass

    @classmethod
    def get_engine_fields(cls, data: dict) -> dict:
        """ """
        schema = cls.get_schema()
        validated_data: dict = schema(**data).to_dict()
        return validated_data
