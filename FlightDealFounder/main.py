from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch
from notification_manager import NotificationManager




""" Type sms if you want to send via sms. """
EMAILAKASMS = "email"
ORIGIN_CITY = "TLV"
NUMBER_OF_MONTHS = 1
## You need to change the EMAIL/PASSWORD in notification_manager.
## You need to change TEQUILA_API_KEY in flight_search.
## You need to add TWILIO_ACC_SID, TWILIO_AUTH_TOK be able to run your code.


flight_search = FlightSearch()
data_manager = DataManager()
notification_manager = NotificationManager()

sheet_data = data_manager.get_destination_data()
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(NUMBER_OF_MONTHS * 30))

""" Un comment to create the iataCode to your cities that you picked """

# if sheet_data[0]["iataCode"] == "":
#     for row in sheet_data:
#         row["iataCode"] = flight_search.get_destination_code(row["city"])
#     print(f"sheet_data:\n {sheet_data}")
#     data_manager.destination_data = sheet_data
#     data_manager.update_codes("iataCode")


""" Un comment to say the how to create the date for flights, today and month later """

# from datetime import datetime
# today = datetime.now()
# month_later = datetime(today.year, today.month+1, today.day)
# print(today, month_later)


""" THIS CODE HELP YOU TO FIND THE BEST PRICES. """

for row in sheet_data:
    flight = flight_search.checkflight(
        origin_city_code=ORIGIN_CITY,
        destination_city_code=row["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    iata_code = row["iataCode"]
    flight_price_current = float(row['lowestPrice'])

    # Found a flight with low price.
    if flight:
        if flight_price_current > flight.price:
            message = f"Low price alert! Only {flight.price} SHEKEL to fly from " \
                      f"{flight.origin_city}-{flight.origin_airport} to " \
                      f"{flight.destination_city}-{flight.destination_airport}," \
                      f" from {flight.out_date} to {flight.return_date}."

            row['lowestPrice'] = flight.price
            if EMAILAKASMS == "email":
                notification_manager.notify_by_email(flight.destination_city, flight.price, message)
            elif EMAILAKASMS == "sms":
                notification_manager.notify_by_sms(flight.destination_city, flight.price, message)
            #Flight with more than one stop.
            if flight.stop_overs > 0:
                message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
                print(message)

data_manager.destination_data = sheet_data
data_manager.update_codes("lowestPrice")

