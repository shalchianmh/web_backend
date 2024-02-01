from rest_framework import serializers
from .models import *
from shop.models import *


class AddPizzaToCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = []

class CartPizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartPizza
        fields = '__all__'

class GetActiveCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaIngredient
        fields = '__all__'

class GetIngredientsOfPizza(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
