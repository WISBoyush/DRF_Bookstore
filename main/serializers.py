from rest_framework import serializers

from tags.models import Tag
from tags.serializers import TagSerializer


class ItemSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    quantity = serializers.IntegerField(required=False)
    title = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    price = serializers.IntegerField(required=False)
    image = serializers.CharField(required=False, allow_blank=True)
    content_type_id = serializers.IntegerField(required=False)
    tags = serializers.ListSerializer(child=serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all()))


class ItemsByCategorySerializer(serializers.Serializer):
    category = serializers.ChoiceField(choices=[('book', 'book'), ('figure', 'figure')])
    item = ItemSerializer()


class BaseDynamicSerializer(serializers.ModelSerializer):
    pass


class TagsDetailSerializer(TagSerializer):
    pass


class BaseGoodSerializer(ItemSerializer):
    pass


class FigureSerializer(BaseGoodSerializer):
    manufacturer = serializers.CharField(required=False)


class BookSerializer(BaseGoodSerializer):
    author = serializers.CharField(required=False)
    date_of_release = serializers.DateField(required=False)
