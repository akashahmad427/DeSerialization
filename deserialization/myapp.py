import requests
import json

URL = "http://127.0.0.1:8000/deserializations/"

data = {
    'name' :'akash',
    'roll' : 120 ,
    'city' : 'lahore'
}

json_data = json.dumps(data)

r = requests.post(url=URL , data=json_data)

data = r.json()

print(data)


