from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('get-profile/', UserProfileView.as_view(), name='get-profile'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('duplicate-username/', DuplicateUsername.as_view(), name='duplicate-username'),
    path('change-address/', ChangeAddress.as_view(), name='change-address'),
]
