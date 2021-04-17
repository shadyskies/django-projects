import requests
import json
from dotenv import load_dotenv
import os


def retrieve():
    load_dotenv()
    apikey = os.getenv('apikey')
    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q=Mumbai&appid={apikey}')
    print(response.text)
    return response.text
