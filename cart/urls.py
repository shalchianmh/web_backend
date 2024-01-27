# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# router = DefaultRouter()
# router.register(r'carts', CartViewSet, basename='cart')

urlpatterns = [
    path('get-active-cart/<pk>', GetActiveCart.as_view(), name='user-active-cart'),
    path('add-good-to-cart/', AddGoodToCart.as_view(), name='add-good-to-cart'),
    path('del-good-from-cart/', DelGoodFromCart.as_view(), name='del-good-from-cart'),
    # path('', include(router.urls)),
    # Other URL patterns as needed
]