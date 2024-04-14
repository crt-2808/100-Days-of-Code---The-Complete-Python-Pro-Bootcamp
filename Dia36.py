import requests
import os
import dotenv
from twilio import Client

dotenv.load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
up_down = None

stock_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": os.getenv("ALPHAVANTAGE_API")
}

news_PARAMS = {
    "qInTitle":COMPANY_NAME,
    "apiKey":os.getenv("NEWS_API")

}

def getNews():
    response_news=requests.get(NEWS_ENDPOINT, params=news_PARAMS)
    response_news.raise_for_status()
    articles=response_news.json()["articles"]
    three_articles=articles[:3]
    formatted_articles=[f"{STOCK}: {up_down}{difference_percentage}%\n Headline:{article["title"]}. \nBrief: {article["description"]}" for article in three_articles]
    client=Client(os.getenv("account_sid"), os.getenv("auth_token"))

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=os.getenv("twilio_phone"),
            to=os.getenv("MY_PHONE")
        )
        print(message.status)


stock_response=requests.get(STOCK_ENDPOINT, params=stock_PARAMS)
stock_response.raise_for_status()
print(stock_response)
data=stock_response.json()["Time Series (Daily)"]
data_list=[value for (key, value) in data.items()]

yesterday_data=data_list[0]
yesterday_closing_price=yesterday_data["4. close"]

before_yesterday_data=data_list[1]
before_yesterday_closing_price=before_yesterday_data["4. close"]


difference=abs(float(yesterday_closing_price)-float(before_yesterday_closing_price))
difference_percentage=round((difference/float(yesterday_closing_price))*100)

if difference>0:
    up_down="⬆️"
else:
    up_down="⬇️"

if difference_percentage>5:
    getNews()

