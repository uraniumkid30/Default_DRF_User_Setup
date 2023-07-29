from django.db.models.query import QuerySet

from conf.core.repositories.base import BaseSelector
from applications.accounts.models import User, UserProfile
from .filters import UserFilter, UserProfileFilter


class UserSelector(BaseSelector):
    @classmethod
    def get_queryset_filter(cls):
        return UserFilter

    @classmethod
    def get_model(cls):
        return User

    @classmethod
    def get_user_login_data(cls, *, user: User):
        return {
            "id": user.id,
            "username": user.username,
            "is_active": user.is_active,
            "is_admin": user.is_admin,
            "is_superuser": user.is_superuser,
        }

    @classmethod
    def list_users(cls, *, filters: dict = {}) -> QuerySet[User]:
        return cls.fetch_records(**filters)


class UserProfileSelector(BaseSelector):
    @classmethod
    def get_queryset_filter(cls):
        return UserProfileFilter

    @classmethod
    def get_model(cls):
        return UserProfile

    @classmethod
    def list_user_profiles(cls, *, filters: dict = {}) -> QuerySet[UserProfile]:
        return cls.fetch_records(**filters)

    @classmethod
    def get_user_profile(cls, *, filters: dict = {}) -> QuerySet[UserProfile]:
        return cls.fetch_record(**filters)
