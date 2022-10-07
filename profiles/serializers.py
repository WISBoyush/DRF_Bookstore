from django.core.validators import RegexValidator
from rest_framework import serializers


class ProfileSerializer(serializers.Serializer):  # noqa

    id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    bio = serializers.CharField(required=False)
    phone = serializers.CharField(
        required=False, validators=[RegexValidator(r'\d{11}', 'Minimum 11', code='invalid')]
    )
    balance = serializers.IntegerField(read_only=True)
    person_disc = serializers.IntegerField(read_only=True)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.save()

        return instance
