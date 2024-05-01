import requests
from bs4 import BeautifulSoup
import re
import smtplib
import dotenv
import os

dotenv.load_dotenv()

Headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept-Language":"es-419,es;q=0.8"
}
URL="https://www.amazon.com.mx/Mimoglad-escritorio-ergon%C3%B3mica-reposacabezas-reposabrazos/dp/B09N93L2RQ/ref=pd_ci_mcx_mh_mcx_views_0?pd_rd_i=B09N93L2RQ"
MY_MAIL=os.getenv("SMTP_MAIL")
MY_PASSWORD=os.getenv("SMTP_PASSWORD")

response=requests.get(url=URL, headers=Headers)
page=response.content

soup=BeautifulSoup(page, "lxml")
price=soup.find(name="span", class_="a-offscreen").text
price_digits = re.sub(r'[^\d.]', '', price)

# Convertir el precio a un número de punto flotante
price_without_currency = float(price_digits)
print(price_without_currency)

contents=f"Hola, este producto esta por debajo del precio que solicitaste, deberias de comprarlo! \n {URL}"
if price_without_currency<3000:
    with smtplib.SMTP(host="smtp.gmail.com", port=587, timeout=120) as connection:
            connection.starttls()
            connection.login(MY_MAIL, MY_PASSWORD)
            connection.sendmail(from_addr=MY_MAIL,
                                to_addrs=MY_MAIL,
                                msg=f"Subject:Alerta de Precio!\n\n{contents}")

