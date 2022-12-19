import requests
from pprint import pprint

SHEETY_ENDPOINT = 'https://api.sheety.co/0130efe4499aa16e1350d344c98f4674/flightDealsV/prices'


class DataManager:
    def __init__(self):
        self.destination = {}

    def get_destination(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        data = response.json()
        pprint(data)
        self.destination = data['prices']
        return self.destination

    def update_sheets(self):
        for city in self.destination:
            new_data = {
                'price': {
                    'iataCode': city['iataCode']
                }
            }
            endpoint = f"{SHEETY_ENDPOINT}/{city['id']}"
            response = requests.put(url=endpoint, json=new_data)
        print(response)