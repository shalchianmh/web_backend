# views.py
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from order.models import *
from .models import *
from rest_framework.views import APIView
from .serializers import *
from . import models


# @permission_classes([IsAuthenticated])
class CalculatePrice(APIView):

    Serializer = PizzaSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        price = 20000
        for k in data.keys():
            qty = data[k]
            ingredient = Ingredient.objects.all().filter(title=k).values('price').first()
            pr = ingredient['price']
            price += qty * pr

        data = {
            "pizza_id": 0,
            "creator": None,
            "image": None,
            "name": None,
            "price": price,
        }
        serializer = PizzaSerializer(data=data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


# def my_view(request):
#     ing = Ingredient(title='cheese', price=10000 ,image=None)
#     ing.save()
#
#     ing = Ingredient(title='pepperoni', price=15000, image=None)
#     ing.save()
#
#     ing = Ingredient(title='olive', price=1000, image=None)
#     ing.save()
#
#     ing = Ingredient(title='corn', price=1000, image=None)
#     ing.save()
#
#     ing = Ingredient(title='mushroom', price=3000, image=None)
#     ing.save()
#
#     ing = Ingredient(title='greenPepper', price=2000, image=None)
#     ing.save()
#
#     ing = Ingredient(title='jambon', price=15000, image=None)
#     ing.save()
#
#     ing = Ingredient(title='bacon', price=20000, image=None)
#     ing.save()
#
#     ing = Ingredient(title='sausage', price=13000, image=None)
#     ing.save()
#
#     ing = Ingredient(title='tomato', price=7000, image=None)
#     ing.save()
#
#



