from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions, status
from rest_framework import generics
from cart.models import *
from shop.models import *
import datetime
# @permission_classes([IsAuthenticated])
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from cart.serializers import *
from rest_framework.permissions import AllowAny


@permission_classes([IsAuthenticated])
class GetActiveCart(APIView):

    pass

@permission_classes([IsAuthenticated])
class AddPizzaToCart(APIView):
    Serializer = AddPizzaToCartSerializer
    def post(self, request, *args, **kwargs):
        user = request.user  # Get the authenticated user

        print(request.user.is_authenticated)
        if user.is_authenticated:
            cart_id = Cart.objects.all().filter(is_current=True).first()
            if cart_id == None:
                date_created = datetime.datetime.now()
                cart = Cart(user=user, is_current=True, date_created=date_created)
                cart_id = cart.cart_id
                cart.save()

            data = request.data
            price = 20000
            for k in data.keys():
                ingredient = Ingredient.objects.all().filter(title=k).values('price').first()
                if ingredient == None:
                    continue
                qty = data[k]
                pr = ingredient['price']
                price += qty * pr

            pizza = Pizza(creator=user, name=data['name'], price=price)
            pizza.save()
            cp = CartPizza(cart=cart_id, pizza=pizza, quantity=1)
            cp.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid'}, status=status.HTTP_401_UNAUTHORIZED)