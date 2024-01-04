
# Rain alert project............
import requests
import os
from twilio.rest import Client

LAT= 28.613939
LON= 77.209023
API_KEY= "api key"

PH_NO= "Phone no from twilio"
ACC_ID= "API ID"
ACC_TOKEN= "API token that u got"

parameters= {
    "lat": "-4.441931",   
    "lon": "15.266293",     
    "appid": "API ID",
    "cnt": 4
}

response= requests.get(url="https://api.openweathermap.org/data/2.5/forecast?", params=parameters)
response.raise_for_status()
data= response.json()          

will_rain= False
for hour_data in data["list"]:
    condition_code= hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain= True
    
if will_rain:
    client = Client(ACC_ID, ACC_TOKEN)
    message = client.messages \
                .create(
                    body="Carry Umbrella, its gonna rain",
                    from_=PH_NO,
                    to= PH_NO)
    
