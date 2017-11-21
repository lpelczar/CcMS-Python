import os

from views.colorful_view import ColorfulView

MENU_OPTIONS = {'1.': 'Restore your password by using token.',
                '2.': 'Exit'}

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

    @staticmethod
    def display_error_message( error_msg: str):
        """
        Method displays error message
        :param error_msg: str -> An error message.
        :return: None
        """
        os.system('clear')
        print(ColorfulView.format_string_to_red(error_msg))
        input(ColorfulView.format_string_to_green(CONFIRM_MESSAGE))

    @staticmethod
    def display_user_token_is_correct_msg():
        print(ColorfulView.format_string_to_green('\nYour token is correct !'))

    @staticmethod
    def display_password_changed_successfully():
        os.system('clear')
        print(ColorfulView.format_string_to_green('You password have been changed successfully'))
        input(ColorfulView.format_string_to_green(CONFIRM_MESSAGE))

    @staticmethod
    def display_that_token_have_been_sent():
        print(ColorfulView.format_string_to_green("You can find the token in your e-mail or SMS box."))
