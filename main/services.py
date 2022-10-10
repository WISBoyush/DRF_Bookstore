from django.contrib.contenttypes.models import ContentType
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED

from main.models import Item
from main.serializers import ItemSerializer, BaseDynamicSerializer
from main.utils import get_4xx_or_error_message_json


class ItemsServiceMixin:
    def get_dynamic_serializer(self, model):
        return type(
            'DynamicItemSerializer',
            (BaseDynamicSerializer, ),
            {'Meta': type('Meta', (), {
                'model': model,
                'fields': '__all__',
            })
             })


    def get_model_for_detail_action(self, item_pk):
        items_instance = Item.objects.get(pk=item_pk)
        return {
            'instance': items_instance,
            'model': ContentType.objects.get(id=items_instance.content_type_id).model_class(),
        }

    def get_model_name_from_ct(self, content_type_id):
        return ContentType.objects.get(id=content_type_id).model_class()


class ItemsService(ItemsServiceMixin):

    def retrieve(self, request, *args, **kwargs):
        actual_item = self.get_model_for_detail_action(kwargs.get('pk'))
        DynamicItemSerializer = self.get_dynamic_serializer(actual_item['model'])
        items_instance = actual_item['model'].objects.get(pk=actual_item['instance'].pk)
        return Response(status=200, data=DynamicItemSerializer(items_instance).data)

    def get_queryset(self):
        return Item.objects.all()

    # def list(self, request, *args, **kwargs):
    #     params = request.query_params.dict()
    #
    #     for key, value in params.items():
    #         params[key] = int(value) if value.isdigit() else value
    #     if params:
    #         return Response(status=200, data=ItemSerializer(Item.objects.filter(**params), many=True).data)
    #     return Response(status=200, data=ItemSerializer(Item.objects.all(), many=True).data)


class GoodsService(ItemsServiceMixin):
    def list(self, model, params=None):
        serializer = self.get_dynamic_serializer(model)
        if params:
            return serializer(model.objects.filter(params), many=True).data
        return Response(status=200, data=serializer(model.objects.all(), many=True).data)

    def get_serializer(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return get_4xx_or_error_message_json(status=HTTP_401_UNAUTHORIZED, message="You have not permission")
        content_type = int(request.data.get('content_type'))
        if content_type not in [8, 9]:
            raise ValueError
        model = self.get_model_name_from_ct(content_type)
        serializer = self.get_dynamic_serializer(model)

        return serializer
