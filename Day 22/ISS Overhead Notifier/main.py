from datetime import datetime
from time import time
import requests
import smtplib

MY_LAT = 12.34567
MY_LONG = 12.34567

iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_response.raise_for_status()

data = iss_response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

def above():
    if MY_LAT-5 <= latitude <= MY_LAT+5 and MY_LONG-5 <= longitude <= MY_LONG+5:
        return True
    else:
        return False
    
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset and time_now <= sunrise:
        return True
    else:
        return False 

while True:
    time.sleep(60)
    if above() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls
        connection.login("test_email", "test_password")
        connection.sendmail(from_addr="test_email",to_addrs="test_email",msg="Subject:Look Up\n\nThe ISS is above you in the sky")