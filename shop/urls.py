from django.urls import path
from .views import *

urlpatterns = [
    # path('pizzas/', PizzaCRUDView.as_view(), name='pizza-crud'),
    # path('pizzas/<pk>', PizzaDetailCRUDView.as_view(), name='pizza-crud'),
    # path('pizzas-by-creator/<pk>', PizzaByCreatorCRUDView.as_view(), name='pizza-by-creator'),
    # path('ingredients/', IngredientCRUDView.as_view(), name='ingredient-crud'),
    # path('ingredients/<pk>', IngredientDetailCRUDView.as_view(), name='ingredient-crud'),
    # path('pizza-ingredients/', PizzaIngredientCRUDView.as_view(), name='pizza-ingredient-crud'),
    # path('pizza-ingredients/<pk>', PizzaIngredientDetailCRUDView.as_view(), name='pizza-ingredient-crud'),
    # path('pizza-ingredients-add/', AddPizzaIngredient.as_view(), name='pizza-ingredient-add'),
    # path('pizza-ingredients-del/', DelPizzaIngredient.as_view(), name='pizza-ingredient-del'),
    # path('my_view/', my_view, name='my_view'),
    path('calculate-price/', CalculatePrice.as_view(), name='calculate-price'),

]
