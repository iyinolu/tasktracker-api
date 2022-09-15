import imp
from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from core import views

router = DefaultRouter(trailing_slash=True)

router.register(r'api/user', views.UserViewSet, basename="user-crud")
router.register(r'api/create', views.CreateUserViewSet, basename="signin")

urlpatterns = [
    path('', include(router.urls))
]