from django.urls import include
from rest_framework.routers import DefaultRouter
from rest_framework.urls import path

from tags.views import TagViewSet

router = DefaultRouter()
router.register('', TagViewSet, basename='tags_tag')

urlpatterns = [
    path('', include(router.urls)),
]
