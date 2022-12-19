#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

datamanager = DataManager()
sheet_data = datamanager.get_destination()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_CODE = 'LON'

if sheet_data[0]['iataCode'] == '':
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row['city'])
    datamanager.destination = sheet_data
    datamanager.update_sheets()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(ORIGIN_CITY_CODE, destination["iataCode"], from_time=tomorrow, to_time=six_month_from_today)
    if flight.price < destination['lowestPrice']:
        notification_manager.send_sms(
            message=f"Low price alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )
