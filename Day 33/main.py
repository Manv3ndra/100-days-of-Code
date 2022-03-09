import requests
from bs4 import BeautifulSoup
import smtplib

headers = {'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 OPR/82.0.4227.50"}

product_url = "https://www.amazon.in/HyperX-Cloud-Alpha-S-Blue/dp/B07X6HDSDY/ref=sr_1_7?crid=3B2BMK8N5ST83&keywords=gaming%2Bheadphones%2Bwired&qid=1646855623&refinements=p_89%3AHyperX&rnid=3837712031&s=computers&sprefix=gaming%2Bheadphones%2Ccomputers%2C421&sr=1-7&th=1"

page = requests.get(product_url, headers=headers)
bs = BeautifulSoup(page.content, "html.parser")

price_int = bs.find("span", class_="a-price-whole").get_text()
price_dec = bs.find("span", class_="a-price-fraction").get_text()
price = float((price_int + price_dec).replace(",",""))
title = bs.find("span", class_="a-size-large product-title-word-break").get_text().strip()

def send_mail():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(your email, your password)

    subject = f"Price of {title} has fallen"
    body = f"The price of {title} has fallen below 100$. Click the link below to buy: \n{product_url}"
    content = f"Subject: {subject}\n\n\n{body}"
    server.sendmail(to email address, from email address, content)

if (price < 7621):
    send_mail()
