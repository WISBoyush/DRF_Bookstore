from django.contrib.contenttypes.models import ContentType
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED

from .models import Item, Figure, Book
from .serializers import ItemSerializer, BookSerializer, FigureSerializer, BaseDynamicSerializer, \
    ItemsByCategorySerializer
from .services import ItemsService
from .utils import get_4xx_or_error_message_json


class BaseViewSet(viewsets.ModelViewSet):

    def get_model_for_detail_action(self, item_pk):
        items_instance = Item.objects.get(pk=item_pk)
        return {
            'instance': items_instance,
            'model': ContentType.objects.get(id=items_instance.content_type_id).model_class(),
        }

    def get_model_name_from_ct(self, content_type_id):
        return ContentType.objects.get(id=content_type_id).model_class()

    def get_dynamic_serializer(self, model):
        return type(
            'DynamicItemSerializer',
            (BaseDynamicSerializer,),
            {'Meta': type('Meta', (), {
                'model': model,
                'fields': '__all__',
            })
             })

    def list_by_category(self, model, params=None):

        serializer = self.get_dynamic_serializer(model)
        if params:
            return serializer(model.objects.filter(params), many=True).data
        return Response(status=200, data=serializer(model.objects.all(), many=True).data)

    def get_serializer(self, request, user_pk, *args, **kwargs):
        if not request.user.is_superuser:
            return get_4xx_or_error_message_json(status=HTTP_401_UNAUTHORIZED, message="You have not permission")
        content_type = int(request.data.get('content_type'))
        if content_type not in [8, 9]:
            raise ValueError
        model = self.get_model_name_from_ct(content_type)
        serializer = self.get_dynamic_serializer(model)

        return serializer

    def get_queryset(self):
        return self.model.objects.all()


class ItemViewSet(BaseViewSet):
    serializer_class = ItemSerializer
    model = Item
    http_method_names = ['get']
    filter_backends = [
        filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter
    ]
    filterset_fields = ['title', 'price']
    search_fields = ['title', 'description']

    # ordering_fields = ['title', 'price']

    def retrieve(self, request, *args, **kwargs):
        item = self.model.objects.filter(id=kwargs.get('pk'))
        instance = item.first()
        items_values = list(item.values())[0]
        category = ContentType.objects.get(id=instance.content_type_id).model
        item_info = {
            'category': category,
            'item': items_values
        }
        serializer = ItemsByCategorySerializer(data=item_info)
        if serializer.is_valid(raise_exception=True):
            return Response(status=200, data=serializer.data)

    def list(self, request, *args, **kwargs):
        service = ItemsService()

        items_info = list(service.extend_items_info())
        serializer = ItemsByCategorySerializer(data=items_info, many=True)
        if serializer.is_valid(raise_exception=True):
            return Response(status=200, data=serializer.data)


class BaseItemActionsViewSet(ItemViewSet):
    http_method_names = ['get', 'post']

    def create(self, request, *args, **kwargs):
        serializer_class = self.get_serializer(request, self.request.user.pk)
        serializer = serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(status=201, data=serializer.data)

    def list(self, request, *args, **kwargs):
        return self.list_by_category(model=self.model, params=self.request.query_params)


class BookViewSet(BaseItemActionsViewSet):
    serializer_class = BookSerializer
    model = Book


class FigureViewSet(BaseItemActionsViewSet):
    serializer_class = FigureSerializer
    model = Figure
