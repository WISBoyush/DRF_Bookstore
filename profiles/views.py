from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.status import HTTP_403_FORBIDDEN
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Profile
from .serializers import ProfileSerializer


class BaseViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsAdminUser)

    def get_queryset(self):
        return self.model.objects.all()


class ProfileViewSet(BaseViewSet):
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated, )
    model = Profile
    http_method_names = ['patch', 'get', 'post']


    def get_queryset(self):
        return self.model.objects.filter(user_id=self.kwargs.get('pk'))

    @action(detail=False, methods=['patch'], url_name='update_profile')
    def update_profile(self, request, *args, **kwargs):
        if self.kwargs.get('pk') != self.request.user.pk:
            return Response(status=403, data='This action is forbidden')
        if 'balance' in request.data and not self.request.user.is_superuser:
            return Response(status=403, data='User is not superuser')
        return self.partial_update(request, *args, **kwargs)

    @action(detail=False, methods=['patch'], url_name='update_balance', permission_classes=[IsAdminUser])
    def update_balance(self, request, *args, **kwargs):
        users_profile = self.model.objects.get(id=self.kwargs.get('pk'))
        users_profile.balance = self.request.data.get('balance')
        users_profile.save()
        return Response(status=200, data=self.serializer_class(users_profile).data)
