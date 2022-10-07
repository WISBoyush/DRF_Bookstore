from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import RentViewSet

rents_router = DefaultRouter()
rents_router.register('', RentViewSet, basename='carts_purchase')

urlpatterns = [
    path('', include(rents_router.urls)),
]
