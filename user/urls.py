from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('get-profile/', UserProfileView.as_view(), name='get-profile'),
    path('create_pizza/', create_pizza, name='create_pizza'),
]
