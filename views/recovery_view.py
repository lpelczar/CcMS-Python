import os
from views.colorful_view import ColorfulView

MENU_OPTIONS = {'1.': 'Start restoring password process',
                '2.': 'Restore password using token',
                '3.': 'Exit'}

CONFIRM_MESSAGE = '\nType ENTER...'

class RecoveryView:


    @staticmethod
    def display_main_menu():
        """
        Method prints main menu of RecoveryController
        :return:
        """
        for number, option in MENU_OPTIONS.items():
            print(number, option)

    @staticmethod
    def get_user_input(prompt: str):
        """
        Method returns user input
        :param prompt: str -> argument for inbuilt input() function
        :return: str -> user input
        """
        return input(prompt)

    def display_error_message(self, error_msg: str):
        """
        Method displays error message
        :param error_msg: str -> An error message.
        :return: None
        """
        os.system('clear')
        print(ColorfulView.format_string_to_red(error_msg))
        input(ColorfulView.format_string_to_green(CONFIRM_MESSAGE))

    def display_user_token_is_correct_msg(self):
        print(ColorfulView.format_string_to_green('\nYour token is correct !'))

