# views.py
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
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

    # cart_item, created = CartItem.objects.get_or_create(cart=cart, good=good)
    # quantity = int(quantity)
    # if not created:
    #     cart_item.quantity += quantity
    #     cart_item.save()
    # else:
    #     CartItem.objects.create(cart=cart, good=good, quantity=quantity)

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






# class CartViewSet(viewsets.ModelViewSet):
#     queryset = Cart.objects.all()
#     serializer_class = CartSerializer
#     permission_classes = [IsAuthenticated]
#
#     @action(detail=False, methods=['post'])
#     def create_cart(self, request):
#         user = request.user
#         cart = Cart.objects.create(user=user, price=0, is_current=True)
#         serializer = CartSerializer(cart)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
#
#
#     @action(detail=True, methods=['post'])
#     def add_good(self, request):
#         user = request.user
#         cart, created = Cart.objects.get_or_create(user=user, is_current=True)
#
#         good_id = request.data.get('good_id')
#         quantity = request.data.get('quantity', 1)
#
#         good = Good.objects.get(pk=good_id)
#
#         cart_item, created = CartItem.objects.get_or_create(cart=cart, good=good)
#
#         if not created:
#             cart_item.quantity += quantity
#             cart_item.save()
#         else:
#             CartItem.objects.create(cart=cart, good=good, quantity=quantity)
#
#         cart.price += good.price * quantity
#         cart.save()
#
#         serializer = CartSerializer(cart)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     @action(detail=True, methods=['post'])
#     def assign_to_order(self, request, pk):
#         user = request.user
#         cart = self.get_object()
#
#         # Create a new order and assign the current cart to it
#         order = Order.objects.create(user=user, cart=cart)
#
#         new_cart = Cart.objects.create(user=user, price=0, is_current=True)
#
#         # Update the old cart to mark it as not current
#         cart.is_current = False
#         cart.save()
#
#         serializer = CartSerializer(new_cart)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#

