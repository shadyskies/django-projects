import requests
import json
from dotenv import load_dotenv
import os
from .models import WeatherModel


def retrieve():
    load_dotenv()
    apikey = os.getenv('apikey')
    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q=Mumbai&appid={apikey}').json()
    save_db(response)
    return WeatherModel.objects.first()


def save_db(response):
    obj = WeatherModel(location='Mumbai', temp=float(response['main']['temp']), feels_like = float(response['main']['feels_like']), pressure=float(response['main']['pressure']), humidity=float(response['main']['humidity']), wind_dir=int(response['wind']['deg']), wind_speed=float(response['wind']['speed']))
    obj.save()
