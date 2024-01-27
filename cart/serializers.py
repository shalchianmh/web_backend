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
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    goods = CartGoodSerializer(many=True)

    class Meta:
        model = Cart
        fields = '__all__'
