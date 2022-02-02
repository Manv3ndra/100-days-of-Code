import pandas

data = pandas.read_csv("Squirell Census.csv")
gray_squirell_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirell_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirell_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [gray_squirell_count, red_squirell_count, black_squirell_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("Squirell Count.csv")