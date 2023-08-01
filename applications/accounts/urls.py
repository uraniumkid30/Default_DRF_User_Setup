from django.conf import settings
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from applications.accounts.api import (
    LoginAPIView,
    UserProfileView,
    UserRegistrationView,
    UserListView,
)


router_v1 = DefaultRouter()
app_name: str = "users"
environment = settings.ENVIRONMENT
urlpatterns = [
    path('', include(router_v1.urls)),
    path('auth/register/', UserRegistrationView.as_view(), name='user-registration'),
    path('auth/login/', LoginAPIView.as_view(), name='user-login'),
    path('auth/user/profile/', UserProfileView.as_view(), name='user-profile'),
    path('auth/users/', UserListView.as_view(), name='user-list'),
]
