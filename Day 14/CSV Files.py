import csv

with open("Weather data.csv") as file:
    data = csv.reader(file)
    temp = []
    for row in data:
        if row[1] != "Temperature":
            print(int(row[1]))