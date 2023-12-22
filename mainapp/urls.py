from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from .views import UserView

router = routers.DefaultRouter()
router.register(r"users", UserView, basename="users")

urlpatterns = [
    path("", include(router.urls)),
]
