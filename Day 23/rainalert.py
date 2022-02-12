import requests
import smtplib

MY_EMAIL = "mprasad_be20@thapar.edu"
MY_PASS = "sanu1801"

url = "http://api.openweathermap.org/data/2.5/onecall/timemachine"
api_key = "b879f898d193822508ddb28b8cdc0c63"
api_params = {
    "lat":31.326015,
    "lon":75.576180,
    "dt":1644602629,
    "appid":api_key,
    "exclude":"current"
}

will_rain = False

response = requests.get(url=url, params=api_params)
data = response.json()
weather_slice = data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 600:
        will_rain = True

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user=MY_EMAIL, password=MY_PASS)

if will_rain:
    connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg="Subject: Your weather report for today\n\nBring an umbrella today")
else:
    connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg="Subject: Your weather report for today\n\nAll good for today")