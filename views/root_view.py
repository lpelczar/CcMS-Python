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
        os.system('clear')
        information_to_creat_new_user = '\nAs new user of our platform you need to sign up with your email and unique password!'
        information_to_sign_in_as_user = '\nAs a user of our platform you need to sign in with your login and password.'

        if sign_up:
            print(information_to_creat_new_user)
        else:
            print(information_to_sign_in_as_user)

    @staticmethod
    def create_user_password():
        user_password = ''
        min_lenght_user_input = 1
        max_lenght_user_input = 30

        correct_input = False
        while not len(user_password) > min_lenght_user_input and len(user_password) < max_lenght_user_input and correct_input:
            user_password = input('Enter your password(it must contain 1 big character and digit, it cant be longer than 30 characters): ')

            for sign in user_password:
                if sign.isdigit():
                    for sign in user_password:
                        if sign.isupper():
                            correct_input = True
                            password = user_password

        return password

    @staticmethod
    def create_user_login():
        user_login = ''
        min_lenght_user_input = 1
        max_lenght_user_input = 30

        while not len(user_login) > min_lenght_user_input and len(user_login) < max_lenght_user_input:
            user_login = input('Enter your login(it cant be longer than 30 characters): ')

        return user_login

    @staticmethod
    def create_user_email():
        user_email = ''
        min_lenght_email = 1
        max_lenght_email = 30

        correct_email_adress = True
        while not len(user_email) > min_lenght_email and len(user_email) < max_lenght_email and correct_email_adress:
            user_email = input('Enter your email adress(it cant be longer than 30 characters): ')
            if re.match(r'[^@]+@[^@]+\.[^@]+', user_email):
                correct_email_adress = False

        return user_email

    @staticmethod
    def create_user_phone_number():
        phone_number = ''
        lenght_number = 9
        correct_phone_number = True

        while correct_phone_number:
            phone_number = input('Enter your phone number: ')
            if phone_number.isdigit() and len(phone_number) == lenght_number:
                correct_phone_number = False

        return phone_number

    @staticmethod
    def get_user_login_password():
        user_login = input('Enter your login: ')
        user_password = input('Enter your password: ')
        login_password = (user_login, user_password)

        return login_password
