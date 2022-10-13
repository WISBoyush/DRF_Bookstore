from rest_framework import serializers

from tags.models import Tag
from tags.serializers import TagSerializer
from .models import Book, Figure


class ItemSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    quantity = serializers.IntegerField(required=False)
    title = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    price = serializers.IntegerField(required=False)
    image = serializers.CharField(required=False)
    content_type_id = serializers.IntegerField(required=False)
    tags = serializers.PrimaryKeyRelatedField(many=True, allow_empty=False, read_only=True, required=False)


class ItemsByCategorySerializer(serializers.Serializer):
    category = serializers.ChoiceField(choices=[('book', 'book'), ('figure', 'figure')])
    item = ItemSerializer()


class BaseDynamicSerializer(serializers.ModelSerializer):
    pass


class FigureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Figure
        fields = '__all__'
    # manufacturer = serializers.CharField(required=False)


class BookSerializer(serializers.ModelSerializer):


    class Meta:
        model = Book
        fields = '__all__'
#     author = serializers.CharField(required=False)
#     date_of_release = serializers.DateField(required=False)

