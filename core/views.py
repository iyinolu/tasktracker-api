from django.shortcuts import render
from rest_framework import viewsets, mixins, generics
from rest_framework.renderers import JSONRenderer
from .models import User
from .serializers import UserSerializer, CreateUserSerializer
from core import serializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CreateUserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer

