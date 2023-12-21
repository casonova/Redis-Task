from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers

from .views import UserView

router =  routers.DefaultRouter()
router.register(r'users', UserView, basename="users")

urlpatterns = [
    path('',include(router.urls)),
    ]