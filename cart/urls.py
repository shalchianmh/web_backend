# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# router = DefaultRouter()
# router.register(r'carts', CartViewSet, basename='cart')

urlpatterns = [
    path('add_good/', add_good, name='add_good'),
    path('pizzas/', PizzaCRUDView.as_view(), name='pizza-crud'),
    path('pizzas/<pk>', PizzaDetailCRUDView.as_view(), name='pizza-crud'),
    path('ingredients/', IngredientCRUDView.as_view(), name='ingredient-crud'),
    path('ingredients/<pk>', IngredientDetailCRUDView.as_view(), name='ingredient-crud'),
    path('pizza-ingredients/', PizzaIngredientCRUDView.as_view(), name='pizza-ingredient-crud'),
    path('pizza-ingredients/<pk>', PizzaIngredientDetailCRUDView.as_view(), name='pizza-ingredient-crud'),
    # path('', include(router.urls)),
    # Other URL patterns as needed
]