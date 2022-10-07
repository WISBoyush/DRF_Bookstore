from rest_framework import serializers

from .models import Item, Book, Figure


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class BaseDynamicItemSerializer(serializers.ModelSerializer):
    pass


class FigureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Figure
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
