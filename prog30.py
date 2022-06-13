import requests
import json

url = "https://api.openweathermap.org/data/2.5/weather?lat=12.97&lon=77.59&appid=b21d3aebec64ca07e5d47b26b8ae42a2"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

d=json.loads(response.text)
print(d["main"]["temp"]-273)
y=round(d["main"]["temp"]-273,2)
print(y)

x={"value":y}

url = "https://io.adafruit.com/api/v2/Shilpika/feeds/temp/data"

payload = "{\"value\":x}\n"
headers = {
    'x-aio-key': "aio_Chno63Hi8fcMJWhmB5wLPlPKthkn",
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "51212191-6ceb-d748-9e8c-855465eb4288"
    }

response = requests.request("POST", url, data=json.dumps(x), headers=headers)

print(response.text)



