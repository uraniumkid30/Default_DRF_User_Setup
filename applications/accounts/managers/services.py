from typing import List

from applications.accounts.models import User, UserProfile
from conf.core.repositories.base import BaseService


class UserService(BaseService):
    @classmethod
    def get_model(cls):
        return User

    @classmethod
    def get_updatable_fields(cls) -> List[str]:
        return None

    @classmethod
    def create_user(
        cls,
        *,
        data: dict = {},
    ) -> User:
        """Creates User"""
        user = cls.create_record(**data)

        return user

    @classmethod
    def update_user(cls, *, user: User, data: dict = {}) -> User:
        update_user, is_updated = cls.create_record(
            user, **data
        )
        return update_user or user


class UserProfileService(BaseService):
    @classmethod
    def get_model(cls):
        return UserProfile

    @classmethod
    def get_updatable_fields(cls) -> List[str]:
        return None

    @classmethod
    def create_user_profile(
        cls,
        *,
        data: dict = {},
    ) -> UserProfile:
        """Creates User Profile"""
        user_profile = cls.create_record(**data)

        return user_profile

    @classmethod
    def update_user_profile(cls, *, user_profile: UserProfile, data: dict = {}) -> UserProfile:
        update_user_profile, is_updated = cls.create_record(
            user_profile, **data
        )
        return update_user_profile or user_profile