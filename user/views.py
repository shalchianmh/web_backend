from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import User
from .serializers import *
from shop.serializers import *

from rest_framework.views import APIView

class CalculatePrice(APIView):

    Serializer = PizzaSerializer
    # Model = models.Pizza

    def post(self, request, *args, **kwargs):
        # return HttpResponse("Hello world!")
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
        print(price)
        serializer = PizzaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)





class RegistrationView(APIView):
    serializer = UserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        login(request, user)

        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class UserProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user = request.user  # Get the authenticated user
        serializer = UserSerializer(user)
        return Response(serializer.data)

