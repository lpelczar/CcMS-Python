import os
import re
import time
from views.colorful_view import ColorfulView


class RootView:

    @staticmethod
    def display_starting_screen(file_name='views/welcome_screen.txt'):
        """
        Argument: str ---> with filename to reader
        Return: None
        """
        os.system('clear')
        with open(file_name) as f:
            reader = f.read()
        print(reader)

    @staticmethod
    def display_main_menu():
        """
        Argument: none
        Return: none

        Method display main menu options.
        """
        welcome_information = '\nWelcome in Canvas, patch 0.-2XYZ.4C version.'
        exit_program = '0. Exit'
        menu_options = ['Sign in', 'Sign up']
        number_option = 1
        welcome_information = ColorfulView.format_string_to_yellow(welcome_information)
        exit_program = ColorfulView.format_string_to_red(exit_program)

        print(welcome_information)

        for option in menu_options:
            option = str(number_option) + '. ' + option
            option = ColorfulView.format_string_to_green(option)
            print(option)
            number_option = int(number_option)
            number_option += 1

        print(exit_program)

    @staticmethod
    def display_sign_menu(sign_up):
        """
        Argument: bool
        Return: none

        Method check if user want to sing in or create new account in platform and display infromation.
        """
        os.system('clear')
        create_new_user_info = '\nAs new user of our platform you need to sign up with your email and unique password!'
        create_new_user_info = ColorfulView.format_string_to_green(create_new_user_info)

        sign_in_as_user_info = '\nAs a user of our platform you need to sign in with your login and password.'
        sign_in_as_user_info = ColorfulView.format_string_to_yellow(sign_in_as_user_info)

        if sign_up:
            print(create_new_user_info)
        else:
            print(sign_in_as_user_info)

    @staticmethod
    def create_user_password():
        max_pass_length = 30
        min_pass_lenght = 5

        incorrect_input = True
        while incorrect_input:
            user_password = input('Enter your password(it must contain big, small characters and digit, it must contain'
                                  'min 6 chars and it cant be longer than 30 characters): ')
            if len(user_password) > min_pass_lenght and len(user_password) < max_pass_length:
                for sign in user_password:
                    if sign.isdigit():
                        for sign in user_password:
                            if sign.isupper():
                                for sign in user_password:
                                    if sign.islower():
                                        incorrect_input = False

        return user_password

    @staticmethod
    def create_user_login():
        """
        Argument: none
        Return: str

        Method check if user login is enter correctly with requirements.
        """
        max_login_lenght = 30
        min_login_lenght = 5

        incorrect_input = True
        while incorrect_input:
            user_login = input('Enter your login(it must contain 6 characters and cant be longer than 30 characters): ')

            if len(user_login) > min_login_lenght and len(user_login) < max_login_lenght:
                incorrect_input = False

        return user_login

    @staticmethod
    def create_user_email():
        """
        Argument: none
        Return: str

        Method check if user email is enter correctly with requirements.
        """
        max_email_lenght = 30
        min_email_lenght = 0

        incorrect_email_adress = True
        while incorrect_email_adress:
            user_email = input('Enter your email adress(it cant be longer than 30 characters): ')

            if len(user_email) > min_email_lenght and len(user_email) < max_email_lenght:
                if re.match(r'[^@]+@[^@]+\.[^@]+', user_email):
                    incorrect_email_adress = False

        return user_email

    @staticmethod
    def create_user_phone_number():
        """
        Argument: none
        Return: str

        Method check if user phone number is digits, and its lenght is 9.
        """
        lenght_number = 9
        incorrect_phone_number = True

        while incorrect_phone_number:
            phone_number = input('Enter your phone number: ')
            if phone_number.isdigit() and len(phone_number) == lenght_number:
                incorrect_phone_number = False

        return phone_number

    @staticmethod
    def get_user_login_password():
        """
        Argument: none
        Return: tuple

        Method take users login and password and return it as a tuple.
        """
        user_login = input('Enter your login: ')
        user_password = input('Enter your password: ')
        login_password = (user_login, user_password)
        return login_password

    @staticmethod
    def add_user_name():
        """
        Argument: None
        Return: str

        Method create users name and return it.
        """
        user_name = input('Enter your name and surname: ')
        return user_name

    @staticmethod
    def display_user_created(login, password, phone_number, email, name):
        """
        Arguments: str, str, str, str, str
        Return: none

        Method display information about created user account.
            """
        os.system('clear')
        print('\nYour succesful creat new account!\n Name: {}\nPhone number: {},'.format(name, phone_number) +
              '\nLogin: {}, \nPassword: {}\nEmail: {}'.format(login, password, email))
        input('Press enter to back')

    @staticmethod
    def display_user_already_exists():
        """
        Argument: none
        Return: none

        Method display information if user already exist.
        """
        os.system('clear')
        print('Entered user already exists!')
        time.sleep(2)

    @staticmethod
    def display_user_not_exist():
        """
        Argument: none
        Return: none

        Method display information about not existing user account
        if someone try to singin with not exist login in database.
        """
        print('User not exists!')
        time.sleep(2)

    @staticmethod
    def display_error_user_singin():
        """
        Argument: none
        Return: none

        Method display infromation when created user try to singin without any status of student, mentor etc.
        """
        os.system('clear')
        print('\nYou try to sing in as random user, please wait for manager or mentor to change your status!')
        print('\n\nWe will inform you when it will be ready.\n\nThank you for patient!')
        time.sleep(4)
