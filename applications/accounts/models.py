import uuid

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)

from .managers import UserManager
from conf.core.models import TimeBaseModel


class User(AbstractBaseUser, PermissionsMixin, TimeBaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=40, null=True, blank=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    phone_no = models.CharField(max_length=15, unique=True)
    email = models.EmailField(blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_no'
    REQUIRED_FIELDS = ['email', 'username', ]
    objects = UserManager()

    def __str__(self):
        # if self.first_name:
        #     return "{}".format(self.first_name)
        return "{}:{}".format(self.username, self.phone_no)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self) -> str:
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self) -> str:
        '''
        Returns the short name for the user.
        '''
        return self.first_name


class Blacklist(TimeBaseModel):
    blacklist = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.blacklist


class UserProfile(TimeBaseModel):
    user = models.OneToOneField(to='User', on_delete=models.CASCADE)

    def __str__(self):
        return "Profile for : {}".format(self.user)
