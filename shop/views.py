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

