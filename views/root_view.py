import os
import re
import sys
import time

from services.password_service import PasswordService
from views.colorful_view import ColorfulView


class RootView:

    @staticmethod
    def display_animate_starting_screen(file_name='views/welcome_screen.txt'):
        """
        Param: str ---> with filename to reader
        Return: None
        """
        os.system('clear')
        main_screen_colored = []

        with open(file_name) as f:
            reader = f.readlines()
            for line in reader:
                line = list(line)
                for item in line:
                    item = ColorfulView.format_ascii(item)
                    print(item, end='')
                    main_screen_colored.append(item)
                    sys.stdout.flush()
                    speed = 0.001
                    time.sleep(speed)

        return main_screen_colored

    def display_main_menu_screen(file_name='views/welcome_screen.txt'):
        """
        Param: str ---> with filename to reader
        Return: None
        """
        os.system('clear')
        with open(file_name) as f:
            reader = f.readlines()
            for line in reader:
                line = list(line)
                for item in line:
                    item = ColorfulView.format_ascii(item)
                    print(item, end='')

    @staticmethod
    def display_main_menu():
        """
        Param: none
        Return: none

        Method display main menu options.
        """
        welcome_information = '\nWelcome in Canvas, patch 0.-2XYZ.4C version.'
        exit_program = '0. Exit'
        menu_options = ['Sign in', 'Sign up', 'Restore password']
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
        Param: bool
        Return: none

        Method check if user want to sign in or create new account in platform and display infromation.
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
        """
        Arguments: none
        Return: none

        Method let to create user his account password and check if it contain requirements.
        """
        incorrect_password = True
        while incorrect_password:
            print(ColorfulView.format_string_to_yellow('Enter your password(it must contain big, small characters and '
                                                       'digit, it must contain min 6 chars and '
                                                       'it cant be longer than 30 characters): '))
            user_password = PasswordService.get_password_with_asterisks()
            if re.match(r'^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])[A-Za-z\d]{6,30}$', user_password):
                incorrect_password = False

        return user_password

    @staticmethod
    def create_user_login():
        """
        Param: none
        Return: str

        Method check if user login is entered correctly with requirements.
        """
        max_login_lenght = 30
        min_login_lenght = 5

        incorrect_input = True
        while incorrect_input:
            print(ColorfulView.format_string_to_yellow('Enter your login(it must contain 6 characters and cant be longer than 30 characters): '))
            user_login = input()

            if len(user_login) > min_login_lenght and len(user_login) < max_login_lenght:
                incorrect_input = False

        return user_login

    @staticmethod
    def create_user_email():
        """
        Param: none
        Return: str

        Method check if user email is enter correctly with requirements.
        """
        max_email_lenght = 30
        min_email_lenght = 0

        incorrect_email_adress = True
        while incorrect_email_adress:
            print(ColorfulView.format_string_to_yellow('Enter your email adress'
                                                       '(it cant be longer than 30 characters): '))
            user_email = input()

            if len(user_email) > min_email_lenght and len(user_email) < max_email_lenght:
                if re.match(r'([A-Za-z\d\.]{1,})([\@]{1})([a-z\d]{1,}[\.]{1}[a-z]{2,})', user_email):
                    incorrect_email_adress = False

        return user_email

    @staticmethod
    def create_user_phone_number():
        """
        Param: none
        Return: str

        Method check if user phone number is digits, and its lenght is 9.
        """
        os.system('clear')
        incorrect_phone_number = True

        while incorrect_phone_number:
            print(ColorfulView.format_string_to_yellow('Enter your phone number: '))
            phone_number = input()

            if re.match(r'\d{3}[\s\\\/\-]?\d{3}[\s\\\/\-]?\d{3}', phone_number):
                incorrect_phone_number = False

        phone_number = RootView.convert_phone_number_to_data_format(phone_number)
        return phone_number

    @staticmethod
    def convert_phone_number_to_data_format(phone_number):
        """
        Method convert phone number to database format.

        Param: str
        Return: str
        """
        format_phone_number = '+48'
        for number in phone_number:
            if number.isdigit():
                format_phone_number += number

        return format_phone_number

    @staticmethod
    def get_user_login_password():
        """
        Param: none
        Return: tuple

        Method take users login and password and return it as a tuple.
        """
        user_login = input('Enter your login: ')
        user_password = PasswordService.get_password_with_asterisks()
        login_password = (user_login, user_password)
        return login_password

    @staticmethod
    def add_user_name():
        """
        Param: None
        Return: str

        Method create users name and return it.
        """
        incorrect = True
        while incorrect:

            print(ColorfulView.format_string_to_yellow('Enter your name and surname: '))
            user_name = input()

            if re.match(r'^(?=[A-Za-z])[\sA-Za-z]{5,30}$', user_name):
                incorrect = False

        return user_name

    @staticmethod
    def display_user_created(login, phone_number, email, name):
        """
        Param: str, str, str, str, str
        Return: none

        Method display information about created user account.
            """
        os.system('clear')
        account_created_info1 = '\nYou have created a new account!\nName: {}\nPhone number: {},'.format(name, phone_number)
        account_created_info2 = '\nLogin: {}, \nEmail: {}'.format(login, email)
        acc_info = account_created_info1 + account_created_info2
        print(ColorfulView.format_string_to_green(acc_info))
        input('Press enter to back')

    @staticmethod
    def display_user_already_exists():
        """
        Param: none
        Return: none

        Method display information if user already exist.
        """
        os.system('clear')
        print(ColorfulView.format_string_to_red('Entered user already exists!'))
        time.sleep(0.5)

    @staticmethod
    def display_user_not_exist():
        """
        Param: none
        Return: none

        Method display information about not existing user account
        if someone try to singin with not exist login in database.
        """
        os.system('clear')
        print(ColorfulView.format_string_to_red('User not exists!'))
        time.sleep(0.5)

    @staticmethod
    def display_error_user_singin():
        """
        Param: none
        Return: none

        Method display infromation when created user try to signing without any status of student, mentor etc.
        """
        os.system('clear')
        print(ColorfulView.format_string_to_green('\nYou are trying to sign in as random user,'
                                                  ' please wait for manager or mentor to change your status!'))
        print(ColorfulView.format_string_to_white('\n\nWe will inform you when it will be ready.'
                                                  '\n\nThank you for patience!'))
        time.sleep(4)
