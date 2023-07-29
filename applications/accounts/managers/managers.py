import string
import random

from django.contrib.auth.models import BaseUserManager

from ..validators import UserValidation

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        UserValidation.email_is_valid(email)
        phone_number = extra_fields.get("phone_no")
        UserValidation.phone_number_is_valid(phone_number)
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        UserValidation.superuser_is_valid(extra_fields.get('is_superuser'))
        return self._create_user(email, password, **extra_fields)


class AuthGen():
    @classmethod
    def createToken(cls, n=8):
        NUMSEQ = string.digits
        token = lambda n: (''.join(random.choice(NUMSEQ) for _ in range(n)))
        return token(n)

    @classmethod
    def uniqueToken(cls, token, tokenbank):
        lock = True
        while lock:
            value = tokenbank.get(token, False)
            lock = True if value else value
        return token
