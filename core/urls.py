import imp
from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from core import views

router = DefaultRouter(trailing_slash=True)
router.register(r'user', views.UserViewSet)
router.register(r'create-user', views.CreateUserViewSet)

urlpatterns = [
    path('', include(router.urls))
]