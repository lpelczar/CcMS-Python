from services.smsapi.client import SmsAPI
from services.smsapi.responses import ApiError
import smtplib


class SmsService:

    @staticmethod
    def send_sms(phone_number, sms_text,  sender='Info'):
        api = SmsAPI()
        api.auth_token = 'ZOqy0r9lKB6sf0HlYnNFtATGUqjaavTPnJFDx1Hx'

        try:
            api.service('sms').action('send')

            api.set_content(sms_text)
            api.set_to(phone_number)
            api.set_from(sender)

            result = api.execute()

            # for r in result:
            #     print(r.id, r.points, r.status)

        except ApiError:
            print('Error encountered while sending message!')


class EmailService:

    @staticmethod
    def send_email(email_text, email):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("kreatywnoscaktywnosc@gmail.com", "kreatywnosc")

        msg = email_text
        server.sendmail("kreatywnoscaktywnosc@gmail.com", email, msg)
