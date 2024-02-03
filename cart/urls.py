# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# router = DefaultRouter()
# router.register(r'carts', CartViewSet, basename='cart')

urlpatterns = [
    path('get-active-cart/', GetActiveCart.as_view(), name='user-active-cart'),
    path('add-pizza-to-cart/', AddPizzaToCart.as_view(), name='add-pizza-to-cart'),
    path('add-exits-pizza-to-cart/', AddExistsPizzaToCart.as_view(), name='add-exits-pizza-to-cart'),
    path('sub-exits-pizza-from-cart/', SubExistsPizzaFromCart.as_view(), name='sub-exits-pizza-from-cart'),
    path('add-to-my-pizza/', AddPizzaToMyPizza.as_view(), name='add-to-my-pizza'),
    path('delete-pizza-from-my-pizza/', DeletePizzaFromMyPizza.as_view(), name='delete-pizza-from-my-pizza'),
    path('add-my-pizza-to-cart/', AddMyPizzaToCart.as_view(), name='add-my-pizza-to-cart'),
    # path('', include(router.urls)),
    # Other URL patterns as needed
]