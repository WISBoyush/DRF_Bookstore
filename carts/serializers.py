from rest_framework import serializers


class CartInnerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    amount = serializers.IntegerField(required=True)
    state = serializers.CharField(read_only=True)
    item_id = serializers.IntegerField(required=True)
    user_id = serializers.IntegerField(read_only=True)
    warranty_days = serializers.IntegerField(required=False)
    orders_id = serializers.CharField(read_only=True)
    orders_time = serializers.DateTimeField(read_only=True)
    city = serializers.CharField(required=False)
    address = serializers.CharField(required=False)
    total_orders_price = serializers.IntegerField(read_only=True)
    price_discounted = serializers.IntegerField(read_only=True)
    new_price = serializers.IntegerField(read_only=True)


class CartOuterSerializer(serializers.Serializer):
    total = serializers.IntegerField(read_only=False)
    persons_discounted_price = serializers.IntegerField(read_only=False)
    products = CartInnerSerializer(many=True)
