from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Tag
from rest_framework.permissions import IsAdminUser

from .serializers import TagSerializer


class BaseTagViewSet(ModelViewSet):
    def get_queryset(self):
        return self.model.objects.all()


class TagViewSet(BaseTagViewSet):
    serializer_class = TagSerializer
    model = Tag
    http_method_names = ['patch', 'get', 'post', 'delete']

    @action(detail=True, methods=['patch', 'get'], url_name='update_tag', permission_classes=[IsAdminUser])
    def update_tag(self, request, *args, **kwargs):
        tag = self.model.objects.filter(id=kwargs.get('pk'))
        if not tag.exists():
            return Response(status=400, data="There is not this tag")
        serialized_data = self.serializer_class(data=request.data, context=self.request)
        serialized_data.is_valid(raise_exception=True)
        tag.update(**request.data)
        return Response(status=200, data="Tag was updated")





