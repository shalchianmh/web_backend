# views.py
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from order.models import *
from .models import *
from .serializers import CartSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_good(request):
    user = request.user
    cart, created = Cart.objects.get_or_create(user=user, is_current=True)

    good_id = request.data.get('good_id')
    quantity = int(request.data.get('quantity', 1))

    good = get_object_or_404(Good, pk=good_id)

    cart_item_queryset = CartItem.objects.filter(cart=cart, good=good)

    if cart_item_queryset.exists():
        # If there are multiple instances, choose the first one
        cart_item = cart_item_queryset.first()
        cart_item.quantity += quantity
        cart_item.save()
    else:
        # If no instance is found, create a new one
        cart_item = CartItem.objects.create(cart=cart, good=good, quantity=quantity)

    cart.price += good.price * quantity
    cart.save()

    serializer = CartSerializer(cart)
    return Response(serializer.data, status=status.HTTP_200_OK)


# views.py
from rest_framework import generics
from .serializers import *


class PizzaCRUDView(
    generics.ListCreateAPIView
):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


class PizzaDetailCRUDView(
    generics.RetrieveUpdateDestroyAPIView
):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


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


class PizzaIngredientCRUDView(
    generics.ListCreateAPIView
):
    queryset = PizzaIngredient.objects.all()
    serializer_class = PizzaIngredientSerializer


class PizzaIngredientDetailCRUDView(
    generics.RetrieveUpdateDestroyAPIView
):
    queryset = PizzaIngredient.objects.all()
    serializer_class = PizzaIngredientSerializer
