from rest_framework import serializers
from .models import *


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


class PizzaIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaIngredient
        fields = ['pizza', 'ingredient', 'quantity']


class PizzaSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True, allow_null=True)

    class Meta:
        model = Pizza
        fields = ['good_id', 'pizza_id', 'name', 'description', 'price', 'ingredients', 'creator']

    def create(self, validated_data):
        ingredients_data = self.context['request'].data.get('ingredients', [])
        pizza = Pizza.objects.create(**validated_data)
        pizza.price = 0
        for ingredient_data in ingredients_data:
            ingredient_id = ingredient_data['ingredient_id']
            quantity = ingredient_data['quantity']
            ingredient = get_object_or_404(Ingredient, ingredient_id=ingredient_id)
            PizzaIngredient.objects.create(pizza=pizza, ingredient=ingredient, quantity=quantity)
            pizza.price += ingredient.price * quantity
        pizza.save()
        return pizza