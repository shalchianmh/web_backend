from rest_framework import serializers
from .models import *


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


class PizzaIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaIngredient
        fields = '__all__'


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = '__all__'