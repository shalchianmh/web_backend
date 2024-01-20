from django.urls import path
from .views import *

urlpatterns = [
    path('get_goods/', get_goods, name='get_goods'),
]
