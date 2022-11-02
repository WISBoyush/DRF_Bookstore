from django.db import transaction
from django.db.transaction import atomic
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from carts.models import Purchase
from carts.serializers import CartSerializer, CartItemSerializer
from main.models import Item
from rents.models import Rent
from rents.serializers import RentSerializer, RentItemSerializer
from .errors import UnexpectedItemError
from .services import CartsService, RentCartsService

from orders.tasks import order_created


class BaseViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return self.model.objects.all()


class CartViewSet(BaseViewSet):
    serializer_class = CartSerializer
    model = Purchase
    http_method_names = ['patch', 'get', 'post', 'delete']
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['patch'], url_path='update_cart')
    def update_cart(self, request, *args, **kwargs):
        items = Item.objects.all()
        if not all(
               [items.filter(id=item['item_id']).exists() for item in self.request.data.get("cart")]
        ):
            return Response(status=400, data="There is not item with this id")

        service = CartsService(self.request.user, self.model)
        datas = service.update_cart(data=self.request.data, *args, **kwargs)
        return Response(status=200, data=CartItemSerializer(datas, many=True).data)

    def list(self, request, *args, **kwargs):
        service = CartsService(self.request.user, self.model)
        returned_data = service.list()

        serialized_datas = self.serializer_class(returned_data, many=False).data

        return Response(status=200, data=serialized_datas)

    @action(detail=False, methods=['post'], url_path='make_order')
    @transaction.atomic()
    def make_order(self, request, *args, **kwargs):
        service = CartsService(self.request.user, self.model)
        try:
            returned_data = service.make_order(
                self.request.data, self.model
            )
        except UnexpectedItemError as e:
            return Response(status=400, data=e)
        else:
            print(f"/////////////////////////////////////////////////////////////\n"
                  f"{returned_data['products'][0]['orders_id']}\n"
                  f"/////////////////////////////////////////////////////////////")
            order_created.delay(
                order_id=returned_data['products'][0]['orders_id']
            )

        serialized_datas = self.serializer_class(returned_data, many=False)

        return Response(status=200, data=serialized_datas.data)


class RentCartViewSet(BaseViewSet):
    serializer_class = RentItemSerializer
    model = Rent
    http_method_names = ['patch', 'get', 'post', 'delete']
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.model.objects.filter(
            user_id=self.request.user.pk,
            state='CART'
        )

    @action(detail=False, methods=['post'], url_path='create_entry')
    def create_entry(self, request, *args, **kwargs):
        service = RentCartsService(self.request.user, self.model)
        try:
            datas = service.create(data=self.request.data, *args, **kwargs)
        except UnexpectedItemError:
            return Response(status=400, data="User can not add to rent cart more than one same item")
        return Response(status=200, data=RentItemSerializer(datas).data)

    @action(detail=False, methods=['post'], url_path='make_order')
    def make_order(self, request, *args, **kwargs):
        service = RentCartsService(self.request.user, self.model)
        returned_data = service.make_order(self.request.data)
        if not returned_data['orders']:
            return Response(status=403, data="There is not any goods in your cart")
        serialized_datas = RentSerializer(returned_data, many=False).data
        return Response(status=200, data=serialized_datas)
