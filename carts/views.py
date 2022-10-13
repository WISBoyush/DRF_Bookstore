from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from carts.models import Purchase
from carts.serializers import CartSerializer, CartItemSerializer
from rents.models import Rent
from rents.serializers import RentSerializer, RentItemSerializer
from .services import CartsService, RentCartsService


class BaseViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return self.model.objects.all()


class CartViewSet(BaseViewSet):
    serializer_class = CartSerializer
    model = Purchase
    http_method_names = ['patch', 'get', 'post', 'delete']

    @action(detail=False, methods=['patch'], url_path='update_cart')
    def update_cart(self, request, *args, **kwargs):
        service = CartsService(self.request.user.pk, self.model)
        datas = service.update_cart(data=self.request.data, user=self.request.user.pk, *args, **kwargs)
        return Response(status=200, data=CartItemSerializer(datas, many=True).data)

    def list(self, request, *args, **kwargs):
        service = CartsService(self.request.user.pk, self.model)
        returned_data = service.list()

        serialized_datas = self.serializer_class(returned_data, many=False).data

        return Response(status=200, data=serialized_datas)

    @action(detail=False, methods=['post'], url_path='make_order')
    def make_order(self, request, *args, **kwargs):
        service = CartsService(self.request.user.pk, self.model)

        returned_data = service.make_order(
            self.request.data, self.model
        )

        serialized_datas = self.serializer_class(returned_data, many=False)

        return Response(status=200, data=serialized_datas.data)


class RentCartViewSet(BaseViewSet):
    serializer_class = RentItemSerializer
    model = Rent
    http_method_names = ['patch', 'get', 'post', 'delete']

    def get_queryset(self):
        return self.model.objects.filter(
            user_id=self.request.user.pk,
            state='CART'
        )

    @action(detail=False, methods=['patch'], url_path='create_entry')
    def create_entry(self, request, *args, **kwargs):
        service = RentCartsService(self.request.user.pk, self.model)
        datas = service.create(data=self.request.data, *args, **kwargs)
        return Response(status=200, data=RentItemSerializer(datas).data)

    @action(detail=False, methods=['post'], url_path='make_order')
    def make_order(self, request, *args, **kwargs):
        service = RentCartsService(self.request.user.pk, self.model)
        returned_data = service.make_order(self.request.data)
        if not returned_data['orders']:
            return Response(status=403, data="There is not any goods in your cart")
        serialized_datas = RentSerializer(returned_data, many=False).data
        return Response(status=200, data=serialized_datas)
