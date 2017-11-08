import os
import re


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

        print(welcome_information)
        for option in menu_options:
            number_option = str(number_option)
            print(number_option + '. ' + option)
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
        information_to_creat_new_user = '\nAs new user of our platform you need to sign up with your email and unique password!'
        information_to_sign_in_as_user = '\nAs a user of our platform you need to sign in with your login and password.'

        if sign_up:
            print(information_to_creat_new_user)
        else:
            print(information_to_sign_in_as_user)

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
        print('\nYour succesful creat new account, with name: {}, phone number: {},'.format(name, phone_number) +
              ' login: {}, password: {} and email!: {}'.format(login, password, email))

    @staticmethod
    def display_user_already_exists():
        print('Entered user already exists!')

    @staticmethod
    def get_option_input():
        return input('Choose option: ')

    @staticmethod
    def display_user_not_exist():
        print('User not exists!')
