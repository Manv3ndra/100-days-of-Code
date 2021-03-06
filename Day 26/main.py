import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth

API_ID = "your_api_id"
API_KEY = "your_api_key"

GENDER = "male"
WEIGHT = 52
HEIGHT = 180
AGE = 19

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
shetty_endpoint = "https://api.sheety.co/05e99ea2a5ae483801c307e5e508327e/myWorkouts/workouts"
exercise_query = input("Which exercises did you do today: ")

exercise_parameters = {
    "query":exercise_query,
    "gender":GENDER,
    "weight_kg":WEIGHT,
    "height_cm":HEIGHT,
    "age":AGE,
}

exercise_headers = {
    "x-app-id":API_ID,
    "x-app-key":API_KEY,
}

response = requests.post(url=exercise_endpoint, json=exercise_parameters, headers=exercise_headers)
data = response.json()

todays_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in data["exercises"]:
    sheet_inputs = {
        "workout":{
            "date":todays_date,
            "time":now_time,
            "exercise":exercise["name"].title(),
            "duration":exercise["duration_min"],
            "calories":exercise["nf_calories"]
        }
    }

sheet_response = requests.post(url=shetty_endpoint, json=sheet_inputs, auth=("your_username","your_password"))
