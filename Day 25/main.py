from datetime import datetime
import requests

url = "https://pixe.la/v1/users"
parameters = {
    "token": "acds13dewqa2",
    "username": "manvendra27",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

""" response = requests.post(url=url, json=parameters)
print(response.text) """

graph_url = "https://pixe.la/v1/users/manvendra27/graphs"
graph_parameters = {
    "id":"graph1",
    "name":"Coding graph",
    "unit":"Hours",
    "type":"int",
    "color":"momiji",
}
graph_header = {
    "X-USER-TOKEN": "acds13dewqa2",
}

""" response = requests.post(url=graph_url, json=graph_parameters, headers=graph_header)
print(response.text) """

pixel_url = "https://pixe.la/v1/users/manvendra27/graphs/graph1"
today_date = datetime(year=2022, month=2, day=13)
pixel_parameters = {
    "date":today_date.strftime("%Y%m%d"),
    "quantity":"2",
}
pixel_header = {
    "X-USER-TOKEN": "acds13dewqa2",
}

""" response = requests.post(url=pixel_url, json=pixel_parameters, headers=pixel_header)
print(response.text) """

update_pixel_url = "https://pixe.la/v1/users/manvendra27/graphs/graph1/20220213"
update_pixel_parameters = {
    "quantity":"1"
}
update_pixel_header = {
    "X-USER-TOKEN": "acds13dewqa2",
}

""" response = requests.put(url=update_pixel_url, json=update_pixel_parameters, headers=update_pixel_header)
print(response.text) """

delete_pixel_url = "https://pixe.la/v1/users/manvendra27/graphs/graph1/20220213"
delete_pixel_header = {
    "X-USER-TOKEN": "acds13dewqa2",
}
response = requests.delete(url=delete_pixel_url, headers=delete_pixel_header)
print(response.text)