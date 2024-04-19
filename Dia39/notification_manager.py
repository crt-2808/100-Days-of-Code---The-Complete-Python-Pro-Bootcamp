from twilio.rest import Client
import dotenv
import os

dotenv.load_dotenv()
TWILIO_SID = os.getenv("account_sid")
TWILIO_AUTH_TOKEN = os.getenv("auth_token")
TWILIO_VIRTUAL_NUMBER = os.getenv("twilio_phone")
TWILIO_VERIFIED_NUMBER = os.getenv("my_phone")

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
