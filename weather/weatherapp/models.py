from django.db import models


class WeatherModel(models.Model):
    location = models.CharField(max_length=20, null=True)
    temp = models.FloatField(max_length=5)
    feels_like = models.FloatField(max_length=5)
    pressure = models.FloatField(max_length=4)
    humidity = models.FloatField(max_length=3)
    wind_dir = models.IntegerField()
    wind_speed = models.FloatField(max_length=5)

    # def __str__(self):
    #     return f"{self.__dict__}"
