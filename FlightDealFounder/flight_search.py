import requests
from datetime import datetime
from pprint import pprint
from flight_data import FlightData

#CHANGE THIS TO YOUR OWN API.
TEQUILA_API_KEY = "QwH-zVwNcKDxogZO8plJ86jeffBuHs0s"

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"



class FlightSearch:

    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def flight_price(self, iata_code):
        today = datetime.now()
        month_later = datetime(today.year, today.month + 1, today.day)

        location_endpoint = f"{TEQUILA_ENDPOINT}/search"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"fly_from": iata_code,
                 "date_from": f"{today.strftime('%d/%m/%y')}",
                 "date_to": f"{month_later.strftime('%d/%m/%y')}",
                 "nights_in_dst_from": 7,
                 "nights_in_dst_to": 30}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def checkflight(self, origin_city_code, destination_city_code, from_time: datetime, to_time: datetime):
        headers = {"apikey": TEQUILA_API_KEY}

        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,  # TO GET THE CHEAPEST.
            "max_stopovers": 0,
            "curr": "ILS"
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search",
                                params=query,
                                headers=headers)
        try:
            data = response.json()['data'][0]
            # pprint(data)

        except IndexError:
            query["max_stopovers"] = 2
            response = requests.get(
                url=f"{TEQUILA_ENDPOINT}/v2/search",
                headers=headers,
                params=query,
            )
            data = response.json()["data"][0]
            # pprint(data)

            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][1]["cityTo"],
                destination_airport=data["route"][1]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][2]["local_departure"].split("T")[0],
                stop_overs=1,
                via_city=data["route"][0]["cityTo"]
            )

            return flight_data
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0])
        print(f"Trip from {flight_data.origin_city} to {flight_data.destination_city} for : {flight_data.price}")
        return flight_data

