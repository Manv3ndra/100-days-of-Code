import datetime as dt
from debugpy import connect
import pandas
import smtplib
import os

os.chdir("D:/My Stuff/100 Days of Code/Day 21")

MY_EMAIL = "test_email"
MY_PASSWORD = "test_password"

now = dt.datetime.now()
today = (now.month, now.day)

data = pandas.read_csv("Auto Birthday Wisher/birthdays.csv")
birthday_dict = {(data_row["month"]): (data_row["day"]) for (index, data_row) in data.iterrows()}

if today in birthday_dict:
    birthday_name = birthday_dict[today]
    file_path = "Auto Birthday Wisher/letter.txt"
    with open(file_path) as letter:
        content = letter.read()
        content = content.replace("[NAME]", birthday_name["name"])
    with smtplib.SMTP("smtp.gmail.com", 587) as connect:
        connect.starttls()
        connect.login(MY_EMAIL, MY_PASSWORD)
        connect.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_name["email"], msg=f"Subject: Happy Birthday\n\n{content}")