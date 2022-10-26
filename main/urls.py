from django.urls import path, include
from rest_framework import routers

from .views import ItemViewSet, BookViewSet, FigureViewSet

routers.DynamicRoute

item_router = routers.DefaultRouter()
item_router.register(r'', ItemViewSet, basename='main_item')

categories_router = routers.SimpleRouter()
categories_router.register(r'book', BookViewSet, basename='main_book'),
categories_router.register(r'figure', FigureViewSet, basename='main_figure'),

urlpatterns = [
    path('items/', include(item_router.urls)),
    path('', include(categories_router.urls)),
]
