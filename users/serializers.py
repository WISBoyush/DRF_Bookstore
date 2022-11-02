from rest_framework import serializers, status
from rest_framework.exceptions import APIException

from users.models import User


class UserSerializer(serializers.Serializer):  # noqa

    id = serializers.IntegerField(read_only=True)
    email = serializers.CharField(required=False)
    password = serializers.CharField(required=False)
    is_active = serializers.BooleanField(required=False)
    is_superuser = serializers.BooleanField(required=False)
    is_staff = serializers.BooleanField(required=False)
    date_joined = serializers.DateTimeField(read_only=True)
    last_login = serializers.DateTimeField(read_only=True)

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise APIException(
                detail="User with this email already exists",
                code=status.HTTP_400_BAD_REQUEST
            )
        return email

    def create(self, validated_data):
        user = User.objects.create_user(
            email=self.initial_data['email'],
            password=self.initial_data['password'],
        )
        return user
