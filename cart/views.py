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


@permission_classes([IsAuthenticated])
class GetActiveCart(
    generics.ListAPIView
):
    serializer_class = CartSerializer
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user, is_current=True)

    def list(self, request, *args, **kwargs):
        cart, created = Cart.objects.get_or_create(user=request.user, is_current=True, defaults={'price':0})
        cart.save()

        serializer = self.get_serializer(cart)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@permission_classes([IsAuthenticated])
class AddGoodToCart(
    generics.CreateAPIView
):
    queryset = CartGood.objects.all()
    serializer_class = CartGoodSerializer

    def create(self, request, *args, **kwargs):
        user = request.user
        cart, created = Cart.objects.get_or_create(user=user, is_current=True, defaults={'price': 0})
        cart.save()
        # cart_id = request.data.get('cart')
        try:
            quantity = int(request.data.get('quantity', 1))
        except:
            return Response({"error": "Invalid quantity format"}, status=status.HTTP_400_BAD_REQUEST)
        good_id = request.data.get('good')
        # try:
        #     cart = Cart.objects.get(pk=cart_id)
        # except Cart.DoesNotExist:
        #     return Response({"error": "Cart not found"}, status=status.HTTP_404_NOT_FOUND)
        try:
            good = Good.objects.get(pk=good_id)
        except Good.DoesNotExist:
            return Response({"error": "Good not found"}, status=status.HTTP_404_NOT_FOUND)
        cart_good, created = CartGood.objects.get_or_create(cart=cart, good=good)
        cart_good.quantity += quantity
        cart.price += quantity * good.price
        cart_good.save()
        cart.save()

        serializer = CartSerializer(cart)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

@permission_classes([IsAuthenticated])
class DelGoodFromCart(
    generics.CreateAPIView
):
    queryset = CartGood.objects.all()
    serializer_class = CartGoodSerializer

    def create(self, request, *args, **kwargs):
        # cart_id = request.data.get('cart')
        user = request.user
        cart, created = Cart.objects.get_or_create(user=user, is_current=True, defaults={'price': 0})
        cart.save()
        good_id = request.data.get('good')
        try:
            quantity = int(request.data.get('quantity', 1))
        except:
            return Response({"error": "Invalid quantity format"}, status=status.HTTP_400_BAD_REQUEST)
        # try:
        #     cart = Cart.objects.get(pk=cart_id)
        # except Cart.DoesNotExist:
        #     return Response({"error": "Cart not found"}, status=status.HTTP_404_NOT_FOUND)
        try:
            good = Good.objects.get(pk=good_id)
        except Good.DoesNotExist:
            return Response({"error": "Good not found"}, status=status.HTTP_404_NOT_FOUND)
        try:
            cart_good = CartGood.objects.get(cart=cart, good=good)

        except CartGood.DoesNotExist:
            return Response({"error": "CartGood not found"}, status=status.HTTP_404_NOT_FOUND)

        if cart_good.quantity < quantity:
            return Response({"error": "CartGood quantity is less than delete amount"},
                            status=status.HTTP_400_BAD_REQUEST)

        cart_good.quantity -= quantity
        cart.price -= quantity * good.price
        cart_good.save()
        cart.save()

        if cart_good.quantity == 0:
            cart_good.delete()
            return Response("deleted successfully", status=status.HTTP_200_OK)
        serializer = CartSerializer(cart)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

























# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def add_good(request):
#     user = request.user
#     cart, created = Cart.objects.get_or_create(user=user, is_current=True)
#
#     good_id = request.data.get('good_id')
#     quantity = int(request.data.get('quantity', 1))
#
#     good = get_object_or_404(Good, pk=good_id)
#
#     cart_item_queryset = CartGood.objects.filter(cart=cart, good=good)
#
#     if cart_item_queryset.exists():
#         # If there are multiple instances, choose the first one
#         cart_item = cart_item_queryset.first()
#         cart_item.quantity += quantity
#         cart_item.save()
#     else:
#         # If no instance is found, create a new one
#         cart_item = CartGood.objects.create(cart=cart, good=good, quantity=quantity)
#
#     cart.price += good.price * quantity
#     cart.save()
#
#     serializer = CartSerializer(cart)
#     return Response(serializer.data, status=status.HTTP_200_OK)
#

