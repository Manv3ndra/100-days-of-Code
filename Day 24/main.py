import requests

MY_EMAIL = "tyour_email"
MY_PASS = "your_password"

STOCK_NAME = "TSLA"
COMPANY = "TESLA"

STOCK_URL  = "https://www.alphavantage.co/query"
NEWS_URL = "https://newsapi.org/v2/everything"

STOCK_ACCESS_KEY = "79PUNB99EG7N6PAU"
NEW_ACCESS_KEY = "1ae63e401d1748689f4111bbdb10155f"

stock_params = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":STOCK_ACCESS_KEY,
}

news_params = {
    "q":COMPANY,
    "searchIn":"title",
    "apiKey":NEW_ACCESS_KEY,
}

def getnews():
    response = requests.get(url=NEWS_URL, params=news_params)
    articles = response.json()["articles"]
    three_articles = articles[:3]
    formatted_articles = [f"Headline: {article['title']}\n\nBrief: {article['description']}" for article in three_articles]
    for article in formatted_articles:
        print(article)

response = requests.get(url=STOCK_URL, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_close = float(yesterday_data["4. close"])
day_before_yesterday_data = data_list[1]
day_before_yesterday_close = float(day_before_yesterday_data["4. close"])
difference = abs(yesterday_close - day_before_yesterday_close)
diff_percent = (difference/float(yesterday_close)) * 100
if (diff_percent > 5):
    getnews()
