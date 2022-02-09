""" import smtplib

my_email = "test_email"
password = "test_password"

with smtplib.SMTP("smtp.gmail.com", 587) as connect:
    connect.starttls()
    connect.login(user=my_email, password=password)
    connect.sendmail(from_addr=my_email, to_addrs=my_email, msg="Subject:Hello\n\nThis is the body of my email")
    connect.close() """

import datetime as dt

print(dt.datetime.now())