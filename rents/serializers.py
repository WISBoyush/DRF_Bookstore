from rest_framework import serializers
from rest_framework.serializers import ListSerializer


class RentItemSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    orders_id = serializers.CharField(read_only=True)
    state = serializers.CharField(read_only=True)
    item_id = serializers.IntegerField(required=False)
    user_id = serializers.IntegerField(read_only=True)
    rented_from = serializers.DateField(read_only=True)
    rented_to = serializers.DateField(read_only=True)
    city = serializers.CharField(required=False)
    address = serializers.CharField(required=False)


class RentSerializer(serializers.Serializer):
    orders_id = serializers.CharField(read_only=True)
    orders = ListSerializer(child=RentItemSerializer())
