from cart.models import *
from cart.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status


@api_view(['GET'])
def get_goods(request):
    goods = Good.objects.all()
    serializer = GoodSerializer(goods, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)