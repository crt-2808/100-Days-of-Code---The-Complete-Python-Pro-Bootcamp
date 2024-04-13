import requests
import datetime as dt
import smtplib
import time

MY_EMAIL= "ramosbarragan.cristian@gmail.com"
MY_PASSWORD="emcdrrstvnmljuqx"
MY_LAT= 19.432608
MY_LGN= -99.133209

parameters={
    "lat": MY_LAT,
    "lng": MY_LGN,
    "formatted": 0
}


def iss_is_up():
    iss_response=requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_latitude=float(iss_response.json()["iss_position"]["latitude"])
    iss_longitude=float(iss_response.json()["iss_position"]["longitude"])
    if ((MY_LAT-5)<=iss_latitude<=(MY_LAT+5)) and ((MY_LGN-5)<=iss_longitude<=(MY_LGN+5)):
        return True


def is_night():
    response=requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    sunset=int(response.json()["results"]["sunset"].split("T")[1].split(":")[0])
    sunrise=int(response.json()["results"]["sunrise"].split("T")[1].split(":")[0])

    today=dt.datetime.now().hour

    if today>= sunset or today<=sunrise:
        return True

def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                        to_addrs="crtram2712@gmail.com",
                        msg=f"Subject:ISS Status \n\n Look to the sky")


while True:
    time.sleep(60)
    if iss_is_up() and is_night():
        send_email() 