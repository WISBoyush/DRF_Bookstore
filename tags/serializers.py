from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.status import HTTP_403_FORBIDDEN

from tags.models import Tag


class TagSerializer(serializers.Serializer):  # noqa

    id = serializers.IntegerField(read_only=True, required=False)
    tag_title = serializers.CharField(read_only=False, required=False)
    tag_description = serializers.CharField(read_only=False, required=False)
    discount = serializers.IntegerField(read_only=False, required=False)

    def create(self, validated_data):
        try:
            tag = Tag.objects.create_user(
                tag_title=self.validated_data['tag_title'],
                tag_description=self.initial_data['tag_description'],
                discount=self.validated_data['discount']
            )
            return tag
        except Exception as e:
            return Response(status=HTTP_403_FORBIDDEN,
                            data=f'message of exception : \"{e}\"')
