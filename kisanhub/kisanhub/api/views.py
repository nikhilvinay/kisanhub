from django_filters.rest_framework import DjangoFilterBackend
from api.serializers import WeatherSerializer
from rest_framework import viewsets
from .models import Weather

class WeatherViewSet(viewsets.ModelViewSet):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('date', 'wtype', 'location',)
