import os
import random
import datetime as dt
import smtplib

os.chdir("D:/My Stuff/100 Days of Code/Day 21")

MY_EMAIL = "test_email"
MY_PASSWORD = "test_password"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 3:
    with open("quotes.txt", "r") as f:
        all_quotes = f.readlines()
        random_quote = random.choice(all_quotes)
        
    with smtplib.SMTP("smtp.gmail.com", 587) as connect:
        connect.starttls()
        connect.login(user=MY_EMAIL, password=MY_PASSWORD)
        connect.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject: Weekly Motivation\n\n{random_quote}")