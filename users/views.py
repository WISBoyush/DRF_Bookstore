import rest_framework.permissions
from rest_framework import viewsets
from rest_framework.decorators import action

from .models import User
from .serializers import UserSerializer


class BaseViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        return self.model.objects.all()


class UserViewSet(BaseViewSet):
    serializer_class = UserSerializer
    model = User
    http_method_names = ['get', 'post', 'patch']
    permission_classes = [rest_framework.permissions.AllowAny, ]

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @action(detail=True, methods=['put'])
    def put(self, request, *args, **kwargs):
        self.update(request, *args, **kwargs)
