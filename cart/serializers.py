from rest_framework import serializers
from .models import *
from django.shortcuts import get_object_or_404





class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = '__all__'


class CartGoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartGood
        fields = ['cart', 'good', 'quantity']


class CartSerializer(serializers.ModelSerializer):
    goods = GoodSerializer(many=True)

    class Meta:
        model = Cart
        fields = '__all__'
