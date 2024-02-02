from django.urls import path
from .views import *

urlpatterns = [
    # path('my_view/', my_view, name='my_view'),
    path('calculate-price/', CalculatePrice.as_view(), name='calculate-price'),
]
