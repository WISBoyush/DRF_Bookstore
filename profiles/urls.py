from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from .views import ProfileViewSet
#
#
# profile_detail = ProfileViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })

router = routers.DefaultRouter()
router.register(r'', ProfileViewSet, basename='profiles_profile')

#
urlpatterns = [
    path('', include(router.urls)),
]
