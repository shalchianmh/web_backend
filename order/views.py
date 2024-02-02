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
from order.models import *


@permission_classes([IsAuthenticated])
class OrderView(APIView):
    def post(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            cart = Cart.objects.all().filter(user=user, is_current=True).first()
            if cart != None:
                date_created = datetime.datetime.now()
                order = Order(user=user , status='Paid' , cart=cart, date_created=date_created)
                order.save()
                Cart.objects.all().filter(user=user, is_current=True).update(is_current=False)
                return Response(data={}, status=status.HTTP_200_OK)
            else:
                return Response(data={'error': 'Invalid'}, status=status.HTTP_401_UNAUTHORIZED)


@permission_classes([IsAuthenticated])
class HistoryView(APIView):
    def post(self, request, *args, **kwargs):
        pass
        # todo