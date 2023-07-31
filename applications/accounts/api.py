import re
import sys
import logging

import jwt
from jwt.exceptions import InvalidSignatureError
from conf.core.api.pagination import CustomPagination
from django.contrib.auth import authenticate, logout
from django.conf import settings

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from applications.accounts.models import User, UserProfile
from applications.accounts.managers.serializers import (
    LoginSerializer,
    RegistrationSerializer,
    ListUserSerializer
)


logger = logging.getLogger(__name__)


class LoginAPIView(APIView):
    """
    Logs in an existing user.
    """
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer
    view_name = sys._getframe(0).f_code.co_name

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')
            verification_token = serializer.validated_data.get('verification_token')
            if verification_token:
                try:
                    user_data = jwt.decode(verification_token, settings.SECRET_KEY, algorithms=['HS256'])
                    user_id = user_data['id']
                    user = User.objects.filter(id=user_id)
                except InvalidSignatureError:
                    user = None

                if user is None or not user.exists():
                    return Response(
                        {'message': "Invalid credentials", 'status': '00'},
                        status=status.HTTP_400_BAD_REQUEST
                    )
            user = authenticate(username=username, password=password)
            if user is None:
                return Response(
                    {'message': "Invalid password", 'status': '00'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            resp = {
                'status': '00',
                'token': user.token, 'id': user.id
            }
            return Response(resp, status=status.HTTP_200_OK)

        return Response({'message': "Invalid credentials", 'status': '00'}, status=status.HTTP_400_BAD_REQUEST)


class UserRegistrationView(APIView):
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            data = {
                'message': "Registration successful",
                "username": user.username,
                "email": user.email,
                "verification_token": user.token
            }
            return Response(data, status=status.HTTP_200_OK)
        return Response({'message': "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = User.objects.get(phone_no=request.user.phone_no)
        data = {'first_name': user.first_name, 'last_name': user.last_name,
                'phone_no': user.phone_no, 'email': user.email,
                }

        if data['first_name'] or data['last_name']:
            message = "Profile is up to date"
        else:
            message = "Profile needs Update"
        return Response({'status': '00', 'user': data, 'message': message})


class UserListView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ListUserSerializer
    # filter_class = UserFilter
    queryset = User.objects.all()
    pagination_class = CustomPagination
