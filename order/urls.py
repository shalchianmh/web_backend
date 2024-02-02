from django.urls import path
from .views import *

urlpatterns = [
    path('order/', OrderView.as_view(), name='order'),
]
