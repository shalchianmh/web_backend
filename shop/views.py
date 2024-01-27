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



class PizzaCRUDView(
    generics.ListCreateAPIView
):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


class PizzaByCreatorCRUDView(
    generics.ListAPIView
):
    serializer_class = PizzaSerializer

    def get_queryset(self):
        return Pizza.objects.filter(creator=self.kwargs['pk'])


class PizzaDetailCRUDView(
    generics.RetrieveUpdateDestroyAPIView
):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


# ingredient view

class IngredientCRUDView(
    generics.ListCreateAPIView
):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class IngredientDetailCRUDView(
    generics.RetrieveUpdateDestroyAPIView
):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


# pizza ingredient view

class PizzaIngredientCRUDView(
    generics.ListAPIView
):
    queryset = PizzaIngredient.objects.all()
    serializer_class = PizzaIngredientSerializer


class PizzaIngredientDetailCRUDView(
    generics.RetrieveUpdateDestroyAPIView
):
    queryset = PizzaIngredient.objects.all()
    serializer_class = PizzaIngredientSerializer


class AddPizzaIngredient(
    generics.CreateAPIView
):
    queryset = PizzaIngredient.objects.all()
    serializer_class = PizzaIngredientSerializer

    def create(self, request, *args, **kwargs):
        pizza_id = request.data.get('pizza')
        try:
            quantity = int(request.data.get('quantity', 1))
        except:
            return Response({"error": "Invalid quantity format"}, status=status.HTTP_400_BAD_REQUEST)
        ingredient_id = request.data.get('ingredient')
        try:
            pizza = Pizza.objects.get(pk=pizza_id)
        except Pizza.DoesNotExist:
            return Response({"error": "Pizza not found"}, status=status.HTTP_404_NOT_FOUND)
        try:
            ingredient = Ingredient.objects.get(pk=ingredient_id)
        except Ingredient.DoesNotExist:
            return Response({"error": "Ingredient not found"}, status=status.HTTP_404_NOT_FOUND)
        pizza_ingredient, created = PizzaIngredient.objects.get_or_create(pizza=pizza, ingredient=ingredient)
        pizza_ingredient.quantity += quantity
        pizza.price += quantity * ingredient.price
        pizza_ingredient.save()
        pizza.save()

        serializer = PizzaSerializer(pizza)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class DelPizzaIngredient(
    generics.CreateAPIView
):
    queryset = PizzaIngredient.objects.all()
    serializer_class = PizzaIngredientSerializer

    def create(self, request, *args, **kwargs):
        pizza_id = request.data.get('pizza')
        try:
            quantity = int(request.data.get('quantity', 1))
        except:
            return Response({"error": "Invalid quantity format"}, status=status.HTTP_400_BAD_REQUEST)
        ingredient_id = request.data.get('ingredient')
        try:
            pizza = Pizza.objects.get(pk=pizza_id)
        except Pizza.DoesNotExist:
            return Response({"error": "Pizza not found"}, status=status.HTTP_404_NOT_FOUND)
        try:
            ingredient = Ingredient.objects.get(pk=ingredient_id)
        except Ingredient.DoesNotExist:
            return Response({"error": "Ingredient not found"}, status=status.HTTP_404_NOT_FOUND)
        try:
            pizza_ingredient = PizzaIngredient.objects.get(pizza=pizza, ingredient=ingredient)

        except PizzaIngredient.DoesNotExist:
            return Response({"error": "PizzaIngredient not found"}, status=status.HTTP_404_NOT_FOUND)

        if pizza_ingredient.quantity < quantity:
            return Response({"error": "PizzaIngredient quantity is less than delete amount"},
                            status=status.HTTP_400_BAD_REQUEST)

        pizza_ingredient.quantity -= quantity
        pizza.price -= quantity * ingredient.price
        pizza_ingredient.save()
        pizza.save()

        if pizza_ingredient.quantity == 0:
            pizza_ingredient.delete()
            return Response("deleted successfully", status=status.HTTP_200_OK)
        serializer = PizzaSerializer(pizza)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)