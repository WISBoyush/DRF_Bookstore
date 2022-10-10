from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from carts.models import Purchase
from orders.errors import OrdersError
from orders.serializers import OrderOuterSerializer
from orders.services import OrderService


class BaseOrderViewSet(ModelViewSet):
    def get_queryset(self):
        return self.model.objects.all()


class OrderViewSet(BaseOrderViewSet):
    serializer_class = OrderOuterSerializer
    model = Purchase
    lookup_url_kwarg = 'orders_id'
    http_method_names = ['patch', 'get', 'post', 'delete']

    def list(self, request, *args, **kwargs):
        service = OrderService()
        data_to_serialize = service.list(user_pk=self.request.user.pk, model=self.model, *args, **kwargs)

        serializer = OrderOuterSerializer(data_to_serialize, many=True)

        return Response(status=200, data=serializer.data)

    @action(detail=False, methods=['get'], url_path="detail")
    def list_detail(self, request, *args, **kwargs):
        service = OrderService()
        orders_id = self.request.data.get('orders_id')
        if not orders_id:
            return Response(status=404, data='Not Found')
        returned_data = service.list_detail(orders_id, self.model, self.request.user.pk)
        serializer = OrderOuterSerializer(returned_data, many=False)
        return Response(status=200, data=serializer.data)

    @action(detail=False, methods=['post'], url_path='pay')
    def pay(self, request, *args, **kwargs):
        service = OrderService()
        orders_id = self.request.data.get('orders_id')
        if not orders_id:
            return Response(status=404, data='Not Found')
        try:
            service.pay(self.request.user.pk, orders_id, self.model)
        except (OrdersError) as e:
            return Response(status=400, data={'message': f'{e}'})

        return Response(status=200, data="Order was successfully created")
