from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from rents.models import Rent
from rents.serializers import RentOuterSerializer
from rents.services import RentService


class BaseOrderViewSet(ModelViewSet):
    def get_queryset(self):
        return self.model.objects.all()


class RentViewSet(BaseOrderViewSet):
    serializer_class = RentOuterSerializer
    model = Rent
    lookup_url_kwarg = 'rents_id'
    http_method_names = ['patch', 'get', 'post', 'delete']

    def list(self, request, *args, **kwargs):
        service = RentService()
        data_to_serialize = service.list(user_pk=self.request.user.pk, model=self.model, *args, **kwargs)

        serializer = self.serializer_class(data_to_serialize, many=True)

        return Response(status=200, data=serializer.data)

    @action(detail=False, methods=['get'], url_path="detail")
    def list_detail(self, request, *args, **kwargs):
        service = RentService()
        orders_id = self.request.data.get('orders_id')
        if not orders_id:
            return Response(status=404, data='Not Found')
        returned_data = service.list_detail(orders_id, self.model, self.request.user.pk)
        serializer = self.serializer_class(returned_data, many=False)
        return Response(status=200, data=serializer.data)

