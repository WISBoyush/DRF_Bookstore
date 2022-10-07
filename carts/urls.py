from django.urls import path, include
from rest_framework import routers

from .views import CartViewSet, RentCartViewSet

router = routers.DefaultRouter()
router.register(r'', CartViewSet, basename='carts_purchase')

rent_router = routers.DefaultRouter()
rent_router.register(r'', RentCartViewSet, basename='rents_rent')

urlpatterns = [
    path('rent/', include(rent_router.urls)),
    path('', include(router.urls)),
]
