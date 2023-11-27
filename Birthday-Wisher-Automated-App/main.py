##################### Extra Hard Starting Project ######################
import random
import pandas as pd
import datetime as dt
import smtplib as smt

MY_EMAIL = "abuhussinfawzi@gmail.com"
PASSWORD = "vmxb znau utuj htqi"

import os
# 1. Update the birthdays.csv

data = pd.read_csv("birthdays.csv")

# Create a dictionary where keys are tuples (month, day) and values are rows
birthday_dict = {(data_row["month"], data_row["day"]): data_row for index, data_row in data.iterrows()}
# print(birthday_dict)


# 2. Check if today matches a birthday in the birthdays.csv
today_tuple = (dt.datetime.now().day, dt.datetime.now().month)


if today_tuple in birthday_dict:
        birth_guy = birthday_dict[today_tuple]
        fl_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
        with open(fl_path) as msg_file:
            content = msg_file.read()
            content = content.replace("[NAME]", birth_guy["name"])
        with smt.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs= birth_guy["email"],
                                msg=f"Subject: Happy Birthday!\n\n {content}")

        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv


# 4. Send the letter generated in step 3 to that person's email address.




