import pandas

data = pandas.read_csv("Weather data.csv")
monday = data[data.Day == "Monday"]
temp = monday.Temperature
print(temp*1.8 + 32)

#create a dataframe
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data_from_dict = pandas.DataFrame(data_dict)
print(data_from_dict)
data_from_dict.to_csv("Data from dict.csv")