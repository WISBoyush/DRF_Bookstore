from django.contrib.contenttypes.models import ContentType
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED

from main.models import Item
from main.serializers import BaseDynamicSerializer
from main.utils import get_4xx_or_error_message_json


class ItemsServiceMixin:

    def get_model_for_detail_action(self, item_pk):
        items_instance = Item.objects.get(pk=item_pk)
        return {
            'instance': items_instance,
            'model': ContentType.objects.get(id=items_instance.content_type_id).model_class(),
        }

    def get_model_name_from_ct(self, content_type_id):
        return ContentType.objects.get(id=content_type_id).model_class()


class ItemsService(ItemsServiceMixin):

    def extend_items_info(self):
        items = Item.objects.all().values()
        for item in items:
            category = ContentType.objects.get(id=item["content_type_id"]).model
            yield {
                'category': category,
                'item': item
            }
