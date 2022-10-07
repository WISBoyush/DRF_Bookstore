from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.status import HTTP_403_FORBIDDEN

from .models import User


class UserSerializer(serializers.Serializer):  # noqa

    email = serializers.CharField(required=False)
    password = serializers.CharField(required=False)
    is_active = serializers.BooleanField(required=False)
    is_superuser = serializers.BooleanField(required=False)
    is_staff = serializers.BooleanField(required=False)
    date_joined = serializers.DateTimeField(read_only=True)
    last_login = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        try:
            user = User.objects.create_user(
                email=self.initial_data['email'],
                password=self.initial_data['password'],
            )
            return user
        except Exception as e:
            return Response(status=HTTP_403_FORBIDDEN,
                            data=f'User authorized under this email already exist \n exception is \"{e}\"')
