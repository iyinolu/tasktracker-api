from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from .models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    renderer_classes = [JSONRenderer]
    
