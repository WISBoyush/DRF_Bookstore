from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import User
from .serializers import UserSerializer


class BaseViewSet(viewsets.ModelViewSet):
    # permission_classes = (, )

    def get_queryset(self):
        return self.model.objects.all()


class UserViewSet(BaseViewSet):
    serializer_class = UserSerializer
    model = User
    http_method_names = ['get', 'post', ]

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    # # def get_queryset(self):
    # #     self.model.objects.filter(id=self.kwargs.get('pk'))
    #
    # def create(self, request, *args, **kwargs):
    #     # self.request.POST._mutable = True
    #     # self.request.data['password'] = make_password(self.request.data['password'])
    #     # self.request.POST._mutable = False
    #     return super().create(request, *args, **kwargs)

    @action(detail=True, methods=['put'])
    def put(self, request, *args, **kwargs):
        self.update(request, *args, **kwargs)
