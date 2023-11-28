import requests
import os
base_url = "https://api.sheety.co"
BEARER = os.getenv("API_Pass_Sheety")
USERNAME = os.getenv("API_Username_Sheety")
PROJECT = "flightDeals"
SHEET = "prices"

class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.headers = {
            "Authorization": f"Bearer {os.getenv('API_Pass_Sheety')}",
            "Content-Type": "application/json",
        }
        self.base_url = "https://api.sheety.co"
        self.project = "flightDeals"
        self.file = "prices"


    def get_destination_data(self):
        # 2. Use the Sheety API to GET all the data in that sheet and print it out.
        endpoint_url = f"/{USERNAME}/{PROJECT}/{SHEET}"
        url = base_url + endpoint_url
        response = requests.get(url=url, headers=self.headers)
        # print(response.text)
        data = response.json()
        print(USERNAME)
        self.destination_data = data["prices"]
        # 3. Try importing pretty print and printing the data out again using pprint() to see it formatted.
        return self.destination_data

    # 6. In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_codes(self, to_update):
        # print({os.getenv('API_Pass_Sheety')})
        endpoint_url = f"/{USERNAME}/{PROJECT}/{SHEET}"
        url = base_url + endpoint_url

        for city in self.destination_data:
            new_data = {
                "price": {
                    f"{to_update}": city[f"{to_update}"]
                }
            }
            response = requests.put(
                url = f"{url}/{city['id']}",
                json=new_data,
                headers = self.headers
            )
            # print(response.text)

