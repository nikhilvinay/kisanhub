from rest_framework import serializers
from .models import Weather

class WeatherSerializer(serializers.Serializer):
    wtype = serializers.CharField()
    location = serializers.CharField(max_length=200)
    date = serializers.DateField()
    value = serializers.DecimalField(max_digits=8, decimal_places=3)

    def create(self, validated_data):
        return Weather.objects.create(**validated_data)

    class Meta:
        model = Weather
        fields = ['wtype', 'location', 'date', 'value']
