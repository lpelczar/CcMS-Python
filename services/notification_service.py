import smtplib

from dependencies.smsapi.client import SmsAPI
from dependencies.smsapi.responses import ApiError


class SmsService:

    @staticmethod
    def send_sms(phone_number, sms_text,  sender='Info'):
        api = SmsAPI()
        api.auth_token = 'QKClng1uYip49EiipXQW1m2AAAi9KgopS9GEnLGP'

        try:
            api.service('sms').action('send')
            api.set_content(sms_text)
            api.set_to(phone_number)
            api.set_from(sender)
            api.execute()

        except ApiError:
            print('Error encountered while sending message!')
        except:
            print('''Unable to send sms, check internet connection or/and contact developer''')


class EmailService:

    @staticmethod
    def send_email(email_text, email):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("kreatywnoscaktywnosc@gmail.com", "kreatywnosc")

        msg = email_text
        server.sendmail("kreatywnoscaktywnosc@gmail.com", email, msg)

SmsService().send_sms('+48577524527', 'Bez internetu')