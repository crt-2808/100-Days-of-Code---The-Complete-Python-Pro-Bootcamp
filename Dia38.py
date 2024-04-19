import requests
import dotenv
import os
import datetime

NUTRIONIX_ENDPOINT="https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT="https://api.sheety.co/41bbb5126cc6ac93d091f19224f27d7f/myWorkouts/workouts"

dotenv.load_dotenv()

today=datetime.datetime.today()
formated_date=today.strftime("%d/%m/%Y")
now_time = datetime.datetime.now().strftime("%X")

excercise=input("Tell me which exersice you did: ")


headers={
    'x-app-id': os.getenv("NUTRITION_APPLICATION_ID"),
    'x-app-key': os.getenv("NUTRITION_APPLICATION_KEYS")
}

Nutrionix_info= {
    "query": excercise,
    "weight_kg": 70,
    "height_cm": 170,
    "age": 24,
}

response=requests.post(url=NUTRIONIX_ENDPOINT, headers=headers, json=Nutrionix_info)
result=response.json()

for exercise in result["exercises"]:
    sheet_inputs={
        "workout":{
            "date": formated_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_response = requests.post(SHEETY_ENDPOINT, json=sheet_inputs, auth=(os.getenv("Sheety_User"), os.getenv("Sheety_Pass")))

print(sheet_response.text)

