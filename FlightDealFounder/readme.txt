Welcome to FlightDeal found program.

This Project is used to  find the lowest cost for flights :
        - Round flights.
        - Flight with specific time (I found it better to find a flight within 2 months.
        - Flight from 7 days to 28.
        - Flight with 1 stop as max.
Notification will be send either to mail or to your phone via sms, you can pick either way to pick
by change the const EMAILAKASMS = "email" or "sms".

You will need to change these consts to work with the program:
1) main:
    ORIGIN_CITY = "TLV", change to your own IATA. (YOU CAN FIND HERE: https://en.wikipedia.org/wiki/IATA_airport_code)
    NUMBER_OF_MONTHS = 1, you can change to whatever you want.
2) notification_manager : change the EMAIL/PASSWORD.
3) flight_search: change TEQUILA_API_KEY to your own
4) add TWILIO_ACC_SID, TWILIO_AUTH_TOK be able to run your code.
5) change the authentication in  sheety to BEARER, and add the username and BEARER to ENV.

API used:
1) TWILIO API.
2) SHEETY API.