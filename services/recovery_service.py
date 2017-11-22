import uuid

from models.user_container import UserContainer
from services.notification_service import EmailService, SmsService
from services.password_service import PasswordService

TOKEN_LENGTH = 8

TOKEN_MESSAGE = "Your token is {} .Use it to restore your password."

class RecoveryService:

    def __init__(self,user_login_or_email: str, token: str = None):
        self.user = UserContainer.get_instance().get_user_by_login_or_email(user_login_or_email)
        self.__raise_exception_if_user_login_or_email_is_incorrect()
        self.__set_token()
        if token:
            self.raise_exception_if_user_token_is_not_correct()

    def send_token_to_user(self):
        """
        Method sends token to user as email and SMS.
        :return: None
        """
        user_email = self.user.email
        message = TOKEN_MESSAGE.format(self.generated_token)
        EmailService.send_email(message, user_email)
        SmsService.send_sms(self.user.phone_number, TOKEN_MESSAGE.format(self.generated_token))


    def __set_token(self):
        """
        Method sets token to new generated one if player starts new recovery password process
        :return: None
        """
        if 'token' in self.user.__dict__:
            self.generated_token = self.user.token
        else:
            self.generated_token = self.generate_new_token()
            self.user.token = self.generated_token
            self.send_token_to_user()
        UserContainer.get_instance().save_users_to_file()

    def generate_new_token(self):
        """
        Method returns random generated token
        :return: str -> token
        """
        return str(uuid.uuid4())[:TOKEN_LENGTH]

    def __raise_exception_if_user_login_or_email_is_incorrect(self):
        """
        Method raises exception if user's login or email is incorrect.
        :param user: User -> user to check
        :return: None
        """
        if not self.user:
            raise AttributeError('User with given login or email does not exist !')

    def raise_exception_if_user_token_is_not_correct(self, token: str):
        """
        Method raises exception if token that user types is incorrect.
        :param token:
        :return: None
        """
        if not self.generated_token == token:
            raise ValueError('This token is not correct !')


    def change_password(self, password: str, token: str):
        """
        Method changes password.
        :param password: str -> user's new password
        :param token: str -> token needed to auth
        :return: None
        """
        self.raise_exception_if_user_token_is_not_correct(token)
        self.user.password = PasswordService.encrypt_password(password)
        delattr(self.user, 'token')
        UserContainer.get_instance().save_users_to_file()

