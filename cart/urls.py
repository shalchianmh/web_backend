# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# router = DefaultRouter()
# router.register(r'carts', CartViewSet, basename='cart')

urlpatterns = [
    path('get-active-cart/', GetActiveCart.as_view(), name='user-active-cart'),
    path('add-pizza-to-cart/', AddPizzaToCart.as_view(), name='add-pizza-to-cart'),
    path('add-pizza-from-cart/', AddPizzaToCart.as_view(), name='add-pizza-from-cart'),
    path('sub-pizza-from-cart/', SubPizzaFromCart.as_view(), name='sub-pizza-from-cart'),
    # path('', include(router.urls)),
    # Other URL patterns as needed
]