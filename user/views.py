from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from .serializers import *
from rest_framework.views import APIView

class RegistrationView(APIView):
    serializer = RegisterSerializer
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
    serializer = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            print(token.key)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class UserProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user = request.user  # Get the authenticated user
        serializer = UserSerializer(user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

class DuplicateUsername(APIView):
    def post(self, request):
        username = request.data['username']
        user = User.objects.all().filter(username=username).first()
        print(user)
        duplicated = 'true'
        if user == None:
            duplicated = 'false'
        else:
            duplicated = 'true'
        return Response(data={'duplicated': duplicated}, status=status.HTTP_200_OK)


@permission_classes([IsAuthenticated])
class LogOutView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        try:
            request.user.auth_token.delete()
            return Response(data={}, status=status.HTTP_200_OK)
        except:
            return Response(data={}, status=status.HTTP_400_BAD_REQUEST)

@permission_classes([IsAuthenticated])
class ChangeAddress(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        try:
            user = request.user
            data = request.data
            User.objects.all().filter(id=user.id).update(address=data['address'])
            return Response(data={}, status=status.HTTP_200_OK)
        except:
            return Response(data={}, status=status.HTTP_400_BAD_REQUEST)




