import os
import string


class RootView:

    @staticmethod
    def display_starting_screen(file_name='welcome_screen.txt'):
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
        exit_program = '\n0. Exit'
        menu_options = ['Sing in', 'Sing up']
        number_option = 1

        print(welcome_information)
        for option in menu_options:
            number_option = str(number_option)
            print(number_option, option)
            number_option = int(number_option)
            number_option += 1
        print(exit_program)

    @staticmethod
    def display_sing_menu():
        os.system('clear')
        min_lenght_user_input = 1
        max_lenght_user_input = 30
        information_to_creat_new_user = '\nAs new user of our platform you need to sing up with ur email and unique password!'
        user_email = ''
        user_password = ''

    @staticmethod
    def display_sing_up_menu():
        print(information_to_creat_new_user)
        while user_email > min_lenght_user_input and user_email < max_lenght_user_input:
            user_email = input('Enter your email adress(it cant be longer than 30 characters): ')

        correct_input = False
        while user_password > min_lenght_user_input and user_password < max_lenght_user_input and correct_input:
            user_password = input('Enter your password(it must contain 1 big character and digit, it cant be longer than 30 characters): ')

            for sign in user_password:
                if sign.isdigit():
                    for sign in user_password:
                        if sign.isupper():
                            correct_input = True

        login_password = (user_email, user_password)
        return login_password

    @staticmethod
    def display_sing_in_menu():
        pass
