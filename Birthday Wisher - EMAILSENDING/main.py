import smtplib
import datetime as dt
import random


# **************************************** SMTP LIB - EMAILING. *************************************

# I have created temp E-mail.
my_email = "abuhussinfawzi@gmail.com"
password = "vmxb znau utuj htqi"

def send_quote_mail(msg):
    global my_email
    global password
    with smtplib.SMTP("smtp.gmail.com") as connection:

        # Transfer Layer Security.
        connection.starttls()
        connection.login(user=my_email, password=password)
        # Send the mail to myself.
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=msg)


# **************************************** DATETIME *************************************

now = dt.datetime.now()
weekday = now.weekday()

# **************************************** QUOTING. *************************************

if weekday == 5:
    with open("quotes.txt") as quote_file:
        quotes = quote_file.readlines()

    todays_quote = random.choice(quotes)
    msg = f"Subject: Saturday's Motivate!\n\n {todays_quote}"

    send_quote_mail(msg)