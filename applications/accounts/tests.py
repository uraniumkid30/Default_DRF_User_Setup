from django.test import TestCase
from .managers.selectors import UserSelector, UserProfileSelector
from .managers.services import UserService


class UserTestCase(TestCase):
    def setUp(self):
        self.valid_user_data: dict = {
            "email": "test@example.com",
            "username": "test username",
            "phone_no": "2909005858",
            "first_name": "test first name",
            "last_name": "test last name",
            "password": "test password",
        }
        self.invalid_user_data: dict = {
            "email": "test@example.com",
            "username": "test username",
            "password": "test password",
        }

    def test_create_valid_user(self):
        user = UserService.create_user(data=self.valid_user_data)
        user_profile = UserProfileSelector.get_user_profile(filters={"user": user})
        fetched_users = UserSelector.list_users()
        fetched_user_profiles = UserProfileSelector.list_user_profiles()
        self.assertIsNotNone(user)
        self.assertIsNotNone(user_profile)
        self.assertIsNotNone(fetched_users)
        self.assertIsNotNone(fetched_user_profiles)
        self.assertEqual(user.username, self.valid_user_data["username"])
        self.assertEqual(user.email, self.valid_user_data["email"])
        self.assertEqual(user.phone_no, self.valid_user_data["phone_no"])
        self.assertEqual(user_profile.user, user)

    def test_create_invalid_user(self):
        user = UserService.create_user(data=self.invalid_user_data)
        self.assertIsNone(user)
