from rest_framework import serializers
from .models import WeatherModel


class WeatherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WeatherModel
        fields = ('location', 'temp', 'feels_like', 'pressure', 'humidity', 'wind_speed', 'wind_dir')