from  twilio.rest import Client
import os
import smtplib

""" Add your TWILIO ACC SID to the Env -> In pyCharm edit configuration and add the ENV"""

TWILIO_ACC_SID = os.getenv('TWILIO_ACC_SID')
TWILIO_AUTH_TOK = os.getenv('TWILIO_AUTH_TOK')

""" I counted a problem in the EMAIL/PASSWORD from ENV - If you solved it feel free to contact me!. """
# EMAIL = os.getenv("EMAIL")
# PASSWORD = os.getenv("PASSWORD")

EMAIL = "abuhussinfawzi@gmail.com"
PASSWORD = "vmxb znau utuj htqi"

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def notify_by_sms(self, msg):
        print(TWILIO_ACC_SID)
        print(TWILIO_AUTH_TOK)
        client = Client(TWILIO_ACC_SID, TWILIO_AUTH_TOK)
        client.messages.create(
            body=msg, from_="+12676139447", to="+972559889507")

    def notify_by_email(self, dest, price, msg):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(EMAIL, PASSWORD)
            connection.sendmail(from_addr=EMAIL,
                                to_addrs=EMAIL,
                                msg=f"Subject: FLIGHT TO {dest} for {price}! \n\n {msg}")
