from rest_framework import serializers, status
from rest_framework.exceptions import APIException
from rest_framework.serializers import raise_errors_on_nested_writes
from rest_framework.utils import model_meta

from tags.models import Tag


class TagSerializer(serializers.Serializer):  # noqa

    id = serializers.IntegerField(read_only=True, required=False)
    tag_title = serializers.CharField(read_only=False, required=False)
    tag_description = serializers.CharField(read_only=False, required=False)
    discount = serializers.IntegerField(read_only=False, required=False)

    def validate_tag_title(self, tag_title):
        print(self.context)
        method = self.context.stream.method
        if Tag.objects.filter(tag_title=tag_title).exists() and method == 'POST':
            raise APIException(
                detail="Tag with this title already exists",
                code=status.HTTP_400_BAD_REQUEST
            )
        return tag_title

    def create(self, validated_data):
        tag = Tag.objects.create(
            tag_title=self.validated_data['tag_title'],
            tag_description=self.initial_data['tag_description'],
            discount=self.validated_data['discount']
        )
        return tag



