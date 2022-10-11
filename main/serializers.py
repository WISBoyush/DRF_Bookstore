from rest_framework import serializers

from tags.serializers import TagSerializer
from .models import Item, Book, Figure


class ItemSerializer(serializers.Serializer):
    quantity = serializers.IntegerField(required=False)
    title = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    price = serializers.IntegerField(required=False)
    image = serializers.CharField(required=False)
    content_type_id = serializers.IntegerField(required=False)


class ItemsByCategorySerializer(serializers.Serializer):
    category = serializers.ChoiceField(choices=[('book', 'book'), ('figure', 'figure')])
    item = ItemSerializer()


class BaseDynamicSerializer(serializers.ModelSerializer):
    pass


class FigureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Figure
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
