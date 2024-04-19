from data_manager import DataManager
from pprint import pprint
from datetime import datetime, timedelta
from flight_search import FlightSearch
from notification_manager import NotificationManager

ORIGIN_CITY_IATA="MEX"
flight_search = FlightSearch()
data_manager=DataManager()
sheet_data=data_manager.get_destination_data()
notification_manager = NotificationManager()

if sheet_data[0]["iataCode"]=="":
    for row in sheet_data:
        row["iataCode"]=flight_search.get_destination_code(row["city"])
    #pprint (f"sheet_data: {sheet_data}")

    data_manager.destination_data=sheet_data
    data_manager.update_destination_code()


tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )