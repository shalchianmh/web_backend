# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# router = DefaultRouter()
# router.register(r'carts', CartViewSet, basename='cart')

urlpatterns = [
    path('add_good/', add_good, name='add_good'),
    # path('', include(router.urls)),
    # Other URL patterns as needed
]
