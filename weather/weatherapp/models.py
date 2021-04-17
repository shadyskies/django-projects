from django.db import models


class WeatherModel(models.Model):
    temperature = models.FloatField(max_length=5)