import requests
import dotenv
import os

dotenv.load_dotenv()

class DataManager:

    def __init__(self):
        self.destination_data={}

    def get_destination_data(self):
        response=requests.get(url="https://api.sheety.co/41bbb5126cc6ac93d091f19224f27d7f/flightDeals/prices", auth=(os.getenv("Sheety_User"), os.getenv("Sheety_Pass")))
        data=response.json()
        self.destination_data=data["prices"]
        return self.destination_data
    
    def update_destination_code(self):
        for city in self.destination_data:
            new_data={
                "price":{
                    "iataCode":city["iataCode"]
                }
            }
            response=requests.put(url=f"https://api.sheety.co/41bbb5126cc6ac93d091f19224f27d7f/flightDeals/prices/{city['id']}", json=new_data, auth=(os.getenv("Sheety_User"), os.getenv("Sheety_Pass")))
            print(response.text)