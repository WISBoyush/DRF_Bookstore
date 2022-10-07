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

    def get_queryset(self):
        return self.model.objects.filter(user_id=self.kwargs.get('pk'))

    def put(self, request, *args, **kwargs):
        if self.kwargs.get('pk') != self.request.user.pk:

            return Response(status=HTTP_403_FORBIDDEN, data='This action is required')
        return self.update(request, *args, **kwargs)
