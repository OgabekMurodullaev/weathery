from rest_framework import serializers

from .models import Weather


class WeatherListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ['id', 'city_name', 'country_name', 'lat', 'lon',
                  'temperature', 'temp_color', 'wind_speed',
                  'wind_color', 'cloud_cover', 'cloud_color']