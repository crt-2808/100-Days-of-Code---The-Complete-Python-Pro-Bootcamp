import smtplib
import datetime as dt
import random

myEmail="ramosbarragan.cristian@gmail.com"
myPassword="emcdrrstvnmljuqx"

def emailSender():
    with open("./Dia32/quotes.txt") as file:
        quotes=[quote.strip() for quote in file.readlines()]
        sendquote=random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=myEmail, password=myPassword) 
        connection.sendmail(
            from_addr=myEmail, 
            to_addrs="0228894@up.edu.mx", 
            msg=f"Subject:Frase del dia\n\n {sendquote}"
            )
        


date=dt.datetime.now()
if date.weekday()==0:
    emailSender()
else:
    print("Not today buddie")

