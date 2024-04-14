import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")
API_KEY = os.getenv("API_KEY")
OM_endpoint="https://api.openweathermap.org/data/2.5/forecast"

MY_LAT= 58.136440
MY_LGN= 52.656109
PARAMS={
    "lat": MY_LAT,
    "lon": MY_LGN,
    "appid": API_KEY,
    "cnt": 4
}
will_rain=False

response=requests.get(OM_endpoint, params=PARAMS)
response.raise_for_status()
wheather_data=response.json()
print(wheather_data["list"][0]["weather"][0]["id"])

for hour_data in wheather_data["list"]:
    condition_code=hour_data["weather"][0]["id"]
    if int(condition_code)<700:
        will_rain=True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="It's gonna rain. Remeber to bring an umbrella ☔",
                     from_='+13344714187',
                     to=os.getenv("MY_PHONE")
                 )
    print(message.status)