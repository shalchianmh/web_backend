from rest_framework import serializers
from cart.models import *
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'phone', 'profile_image')

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')

# class PizzaSerializer(serializers.ModelSerializer):
#     ingredients = serializers.PrimaryKeyRelatedField(many=True, queryset=Ingredient.objects.all(), required=False)
#     class Meta:
#         model = Pizza
#         fields = ('name', 'ingredients')
#
#


