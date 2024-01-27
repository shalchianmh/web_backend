# views.py
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from order.models import *
from .models import *
from rest_framework import generics
from .serializers import *


# class PizzaCRUDView(
#     generics.ListCreateAPIView
# ):
#     queryset = Pizza.objects.all()
#     serializer_class = PizzaSerializer
#
#
# class PizzaByCreatorCRUDView(
#     generics.ListAPIView
# ):
#     serializer_class = PizzaSerializer
#
#     def get_queryset(self):
#         return Pizza.objects.filter(creator=self.kwargs['pk'])
#
#
# class PizzaDetailCRUDView(
#     generics.RetrieveUpdateDestroyAPIView
# ):
#     queryset = Pizza.objects.all()
#     serializer_class = PizzaSerializer


# ingredient view

# class IngredientCRUDView(
#     generics.ListCreateAPIView
# ):
#     queryset = Ingredient.objects.all()
#     serializer_class = IngredientSerializer
#
#
# class IngredientDetailCRUDView(
#     generics.RetrieveUpdateDestroyAPIView
# ):
#     queryset = Ingredient.objects.all()
#     serializer_class = IngredientSerializer
#
#
# class PizzaIngredientCRUDView(
#     generics.ListAPIView
# ):
#     queryset = PizzaIngredient.objects.all()
#     serializer_class = PizzaIngredientSerializer
#
#
# class PizzaIngredientDetailCRUDView(
#     generics.RetrieveUpdateDestroyAPIView
# ):
#     queryset = PizzaIngredient.objects.all()
#     serializer_class = PizzaIngredientSerializer
#

###############################
### aboves are so dangerous ###
###############################


# @permission_classes([IsAuthenticated])
class CalculatePrice(
    generics.CreateAPIView
):
    serializer_class = PizzaSerializer

    def create(self, request, *args, **kwargs):
        print(request.data)
        price = 10000 * request.data.get('cheese')
        serializer = PizzaSerializer(price)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
