from rest_framework import serializers
from .models import *



class CartPizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartPizza
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
