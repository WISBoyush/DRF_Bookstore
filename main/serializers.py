from rest_framework import serializers

from .models import Item, Book, Figure


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
    # quantity = serializers.IntegerField(required=False)
    # title = serializers.CharField(required=False)
    # description = serializers.CharField(required=False)
    # price = serializers.IntegerField(required=False)
    # image = serializers.ImageField(required=False)
    # tags = serializers.CharField(required=False)
    # content_type = serializers.CharField(required=False)


#
# class DetailItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ContentType
#
#     id = serializers.IntegerField(
#         validators=[
#             RegexValidator(
#                 r'[8-9]'
#             )
#         ],
#     )
#     model = serializers.CharField(read_only=True)
#     app_label = serializers.CharField(read_only=True)


class BaseDynamicItemSerializer(serializers.ModelSerializer):
    pass

    # author = serializers.CharField(read_only=True)
    # date_of_release = serializers.DateField(read_only=True)


#
#     # items_info = serializers.SerializerMethodField()
#     #
#     # def get_accounts_items(self, obj):
#     #     items_main_info = Book.objects.filter(
#     #         item_ptr_id=obj.id)
#     #     serializer = ItemSerializer(items_main_info, many=True)
#     #
#     #     return serializer.data
#
#
class FigureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Figure
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


# manufacturer = serializers.CharField(read_only=True)
# items_info = serializers.SerializerMethodField()
#
# def get_accounts_items(self, obj):
#     items_main_info = Figure.objects.filter(
#         item_ptr_id=obj.id)
#     serializer = ItemSerializer(items_main_info, many=True)
#
#     return serializer.data
