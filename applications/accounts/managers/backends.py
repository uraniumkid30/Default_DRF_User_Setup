from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from django.db.models import Q
from django.contrib.auth import get_user_model

MyUser = get_user_model()


class SettingsBackend(BaseBackend):
    """
    Authenticate against the settings ADMIN_LOGIN and ADMIN_PASSWORD.

    Use the login name and a hash of the password. For example:

    ADMIN_LOGIN = 'admin'
    ADMIN_PASSWORD = 'pbkdf2_sha256$30000$Vo0VlMnkR4Bk$qEvtdyZRWTcOsCnI/oQ7fVOu1XAURIZYoOZ3iq8Dr4M='
    """

    def authenticate(self, request, username=None, password=None):
        # login_valid = settings.ADMIN_LOGIN == username
        # pwd_valid = check_password(password, settings.ADMIN_PASSWORD)
        # if login_valid and pwd_valid:
        try:
            user = MyUser.objects.get(Q(username=username)|Q(email=username)|Q(phone_no=username))
            
        except MyUser.DoesNotExist:
            # Create a new user. There's no need to set a password
            # because only the password from settings.py is checked.
            pass
        else:
            if user.check_password(password):
                user.save()
                return user
        return None

    def get_user(self, user_id):
        try:
            return MyUser.objects.get(pk=user_id)
        except MyUser.DoesNotExist:
            return None