import requests
import json


response = requests.get("http://127.0.0.1:8000/hero/heros/")
heros = json.loads(response.text)

with open('json_file.json', 'w') as file:
    json.dump(heros, file, indent=4, sort_keys=True)