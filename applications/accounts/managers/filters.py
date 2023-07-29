import django_filters

from applications.accounts.models import User, UserProfile


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = {
            "id": ["exact", "isnull"],
            "username": ["iexact", "isnull"],
            "is_superuser": ["exact", "isnull"],
        }


class UserProfileFilter(django_filters.FilterSet):
    class Meta:
        model = UserProfile
        fields = "__all__"
