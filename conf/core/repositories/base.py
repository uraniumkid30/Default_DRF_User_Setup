from abc import ABC, abstractmethod
from typing import Any, Dict, List, Tuple, Iterable

from django.db import models
from django.db import transaction
from django.db.models import Model
from django_filters import FilterSet
from django.db.models.query import QuerySet

from conf.core.repositories.exceptions import FetchError
from conf.core.types import DjangoModelType


class BaseSelector(ABC):
    @classmethod
    @abstractmethod
    def get_queryset_filter(cls) -> FilterSet:
        """Define the django filter created for the given model"""
        pass

    @classmethod
    @abstractmethod
    def get_model(cls) -> DjangoModelType:
        """define the model to be interfaced with"""
        pass

    @classmethod
    def fetch_records(cls, filter_directly=True, **filters) -> QuerySet:
        """Fetch all rows from db"""
        model = cls.get_model()
        query = result = model.objects.filter(**filters)
        if not filter_directly:
            queryset_filter = cls.get_queryset_filter()
            filter_object = queryset_filter(filters, query)
            result = filter_object.qs
        return cls.__get_result(result)

    @classmethod
    def fetch_record(cls, raise_exception=True, **filters) -> Model:
        """Fetch one row from db"""
        try:
            model = cls.get_model()
            result = model.objects.get(**filters)
        except model.DoesNotExist:
            result = None
        except Exception as err:
            print(f"Error fetching record {err}")
            result = None
        return cls.__get_result(result, raise_exception=raise_exception)

    @classmethod
    def fetch_first_record(cls, **filters) -> Model:
        """Fetch first row from db"""
        result = cls.fetch_records(**filters).first()
        return cls.__get_result(result)

    @classmethod
    def fetch_last_record(cls, **filters) -> Model:
        """Fetch last row from db"""
        result = cls.fetch_records(**filters).last()
        return cls.__get_result(result)

    @staticmethod
    def __get_result(result, raise_exception=False):
        if (result is None or not result) and raise_exception:
            raise FetchError
        return result

    @classmethod
    def dictfetchall(cls, cursor) -> list:
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]


class BaseService(ABC):
    @classmethod
    @abstractmethod
    def get_model(cls) -> DjangoModelType:
        pass

    @classmethod
    @abstractmethod
    def get_updatable_fields(cls) -> List[str]:
        pass

    @classmethod
    @transaction.atomic
    def delete_record(cls, *, instance: DjangoModelType) -> bool:
        try:
            instance.delete()
        except Exception as err:
            print(f"Error deleting record {err}")
            is_deleted = False
        else:
            is_deleted = True
        return is_deleted

    @classmethod
    @transaction.atomic
    def update_record(
        cls, *, instance: DjangoModelType, data: Dict[str, Any]
    ) -> Tuple[DjangoModelType, bool]:
        updatable_fields = cls.get_updatable_fields()
        return cls.model_update_record(
            instance=instance, fields=updatable_fields, data=data
        )

    @classmethod
    @transaction.atomic
    def create_record(cls, save_now=True, **data) -> DjangoModelType:
        try:
            model = cls.get_model()
            created_record = model(**data)
            created_record.full_clean()
            if save_now:
                created_record.save()
            return created_record
        except Exception as err:
            print(f"Error in creating database record: {err}")

    @classmethod
    def model_update_record(
        cls, *, instance: DjangoModelType, fields: List[str], data: Dict[str, Any]
    ) -> Tuple[DjangoModelType, bool]:
        """
        Generic update service meant to be reused in local update services.
        For example:
        def receipt_update(*, receipt: Receipt, data) -> Receipt:
            fields = ['store', 'line_item', "currency]
            updated_receipt, has_updated = model_update(instance=receipt, fields=fields, data=data)
            // Do other actions with the user here
            return updated_receipt
        Return value: Tuple with the following elements:
            1. The instance we updated.
            2. A boolean value representing whether we performed an update or not.
        Some important notes:
            - Only keys present in `fields` will be taken from `data`.
            - If something in present in `fields` but not present in `data`, we simply skip.
            - There's a strict assertion that all values in `fields` are actual fields in `instance`.
            - `fields` can support m2m fields, which are handled after the update on `instance`.
        """
        has_updated = False
        m2m_data = {}
        update_fields = []
        try:
            model_fields = {field.name: field for field in instance._meta.get_fields()}
            updatable_fields: Iterable = fields or data.keys()
            for field in updatable_fields:
                # Skip if a field is not present in the actual data
                if field not in data:
                    continue

                # If field is not an actual model field, raise an error
                model_field = model_fields.get(field)

                assert (
                    model_field is not None
                ), f"{field} is not part of {instance.__class__.__name__} fields."

                # If we have m2m field, handle differently
                if isinstance(model_field, models.ManyToManyField):
                    m2m_data[field] = data[field]
                    continue

                if getattr(instance, field) != data[field]:
                    has_updated = True
                    update_fields.append(field)
                    setattr(instance, field, data[field])

            # Perform an update only if any of the fields were actually changed
            if has_updated:
                instance.full_clean()
                # Update only the fields that are meant to be updated.
                # Django docs reference:
                # https://docs.djangoproject.com/en/dev/ref/models/instances/#specifying-which-fields-to-save
                instance.save(update_fields=update_fields)

            for field_name, value in m2m_data.items():
                related_manager = getattr(instance, field_name)
                related_manager.set(value)
                has_updated = True
        except Exception as err:
            print(f'update error {err} for {instance}')

        return instance, has_updated
