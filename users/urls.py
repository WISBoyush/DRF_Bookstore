from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from .views import UserViewSet
#
api_router = routers.DefaultRouter()
api_router.register(r'', UserViewSet, basename='users_user')

#
urlpatterns = [
    path('', include(api_router.urls)),
    path('<int:pk>/profile/', include('profiles.urls'))
]
