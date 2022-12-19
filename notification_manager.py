from twilio.rest import Client
ACCOUNT_SID ='AC99a12b970f35bebe47e7f5cdd25b2b22'
TWILIO_PHONE_NO = '12184005996'
AUTH_TOKEN = 'e485f20b700d619b7557a7b9b2882d4e'


class NotificationManager:
    def __init__(self):
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body= message,
            from_=TWILIO_PHONE_NO,
            to='+14388621036',
        )
        print(message.sid)
