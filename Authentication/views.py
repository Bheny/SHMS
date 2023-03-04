from django.shortcuts import render

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserSerializer

class CreateUserView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

class ObtainTokenPairWithColorView(TokenObtainPairView):
    serializer_class = TokenPairColorSerializer

class TokenPairColorSerializer(serializers.Serializer):
    color = serializers.CharField(max_length=10)

    def validate(self, attrs):
        data = super().validate(attrs)
        data['color'] = attrs['color']
        return data

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['color'] = user.color  # Add custom claim
        return token
