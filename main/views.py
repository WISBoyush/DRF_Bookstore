from rest_framework import viewsets
from rest_framework.response import Response

from .models import Item, Figure, Book
from .serializers import ItemSerializer, BaseDynamicItemSerializer, BookSerializer, FigureSerializer
from .services import GoodsService, ItemsService


class BaseViewSet(viewsets.ModelViewSet):

    def get_dynamic_serializer(self, model):
        return type(
            'DynamicItemSerializer',
            (BaseDynamicItemSerializer,),
            {'Meta': type('Meta', (), {
                'model': model,
                'fields': '__all__',
            })
             })

    def get_queryset(self):
        return self.model.objects.all()


class ItemViewSet(BaseViewSet):
    serializer_class = ItemSerializer
    model = Item
    http_method_names = ['get']

    def retrieve(self, request, *args, **kwargs):
        service = ItemsService()
        return service.retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        service = ItemsService()
        return service.list(request, *args, **kwargs)


class BaseItemActionsViewSet(ItemViewSet):
    http_method_names = ['get', 'post']

    def create(self, request, *args, **kwargs):
        service_class = GoodsService()
        serializer_class = service_class.get_serializer(request, self.request.user.pk)
        serializer = serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(status=201, data=serializer.data)

    def list(self, request, *args, **kwargs):
        service_class = GoodsService()
        return service_class.list(model=self.model, params=self.request.query_params)


class BookViewSet(BaseItemActionsViewSet):
    serializer_class = BookSerializer
    model = Book


class FigureViewSet(BaseItemActionsViewSet):
    serializer_class = FigureSerializer
    model = Figure
