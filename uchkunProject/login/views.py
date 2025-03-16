from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework.authtoken.views import ObtainAuthToken

# Создание токена при входе пользователя
class LoginView(ObtainAuthToken):
    permission_classes = (AllowAny)
    
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user_id': user.pk,
                'user_type': user.user_type
            })
        return Response({"error": "Неверные учетные данные"}, status=status.HTTP_400_BAD_REQUEST)

