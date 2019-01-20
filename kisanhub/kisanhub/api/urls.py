from django.contrib import admin
from django.urls import path, include
from api.views import WeatherViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api', WeatherViewSet)

urlpatterns = [
    path('', include(router.urls))
]
