import os

from dependencies.texttable import Texttable, get_color_string, bcolors
from views.colorful_view import ColorfulView

STARTING_INDEX = 1
MENU_OPTIONS = {'1.': 'Promote user to Mentor',
                '2.': 'Remove Mentor',
                '3.': 'Edit Mentor data',
                '4.': 'Display list of Mentors',
                '5.': 'Display list of Students',
                '6.': 'Display all Canvas members',
                '7.': 'Change Canvas member role',
                '8.': 'Send email to all',
                '0.': 'Log out'}
COLORED_MENU_OPTIONS = {get_color_string(bcolors.PURPLE, k): get_color_string(bcolors.PURPLE, v)
                        for k, v in MENU_OPTIONS.items()}


class ManagerView:

    @staticmethod
    def display_manager_menu(user_login, role):
        """
        Print manager menu
        :param user_login: string -> login of the user
        :param role: string -> role of the user
        :return:
        """
        greeting_message = get_color_string(bcolors.BLUE, 'Logged as {} ({})'.format(user_login, role))
        t = Texttable()
        t.set_deco(Texttable.HEADER)
        t.add_rows([['', greeting_message]] +
                   [[k, v] for k, v in COLORED_MENU_OPTIONS.items()])
        print(t.draw())

    @staticmethod
    def get_option_input():
        """
        Get user input about option in menu
        :return: string
        """
        return input(get_color_string(bcolors.BLUE, '\nChoose an option: '))

    @staticmethod
    def display_actual_list(users):
        """
        Display list of users in table
        :param users: list of users
        :return:
        """
        print('')
        ManagerView.print_table(users)
        print('')

    @staticmethod
    def print_table(users):
        """
        Print table of users using texttable module
        :param users: list of users
        :return:
        """
        t = Texttable()
        t.set_cols_dtype(['a', 'a', 'a', 'a', 'i', 'a'])
        colored_titles = [get_color_string(bcolors.BLUE, i) for i in ['Index', 'Login', 'Name', 'Role',
                                                                      'Phone Number', 'E-mail']]
        t.add_rows([colored_titles] +
                   [[i + STARTING_INDEX, u.get_login(), u.get_name(), u.__class__.__name__, u.get_phone_number(),
                     u.get_email()] for i, u in enumerate(users)])
        print(t.draw())

    @staticmethod
    def display_empty_list_message():
        """
        Display message about empty list
        :return:
        """
        print('')
        print(ColorfulView.format_string_to_red('List is empty!'))
        input('\nPress ENTER to continue')

    @staticmethod
    def display_users(users):
        """
        Print all users in table
        :param users: list of users
        :return:
        """
        print('')
        ManagerView.print_table(users)
        input('\nPress ENTER to continue')

    @staticmethod
    def display_mentor_information(mentor_data):
        """
        Display information about mentor
        :param mentor_data: mentor object
        :return:
        """
        os.system('clear')
        print(ColorfulView.format_string_to_yellow('Login: ') + mentor_data.get_login()
              + ColorfulView.format_string_to_green('\nName: ') + mentor_data.get_name()
              + ColorfulView.format_string_to_green('\nPhone number: ') + mentor_data.get_phone_number()
              + ColorfulView.format_string_to_green('\nEmail: ') + mentor_data.get_email())

    @staticmethod
    def get_promotion_input():
        """
        Get login of user to promote to Mentor
        :return:
        """
        return input('Enter login of the user which do you want to promote to Mentor: ')

    @staticmethod
    def get_user_remove_input():
        """
        Get login of user to remove
        :return:
        """
        return input('Enter login of the user which do you want to remove: ')

    @staticmethod
    def get_user_edit_input():
        """
        Get login of mentor to modify
        :return:
        """
        return input('Enter login of the mentor which do you want to modify: ')

    @staticmethod
    def get_new_value():
        """
        Get new value of user attributes to change
        :return:
        """
        return input('Enter new value: ')

    @staticmethod
    def display_wrong_attribute():
        """
        Display message about wrong attribute typed
        :return:
        """
        print(ColorfulView.format_string_to_red('There is no such attribute to change!'))
        input('\nPress ENTER to continue')

    @staticmethod
    def display_user_promoted(user):
        """
        Display information that user has been promoted
        :param user: User object
        :return:
        """
        print(ColorfulView.format_string_to_green('User: {} has been promoted'.format(user.get_login())))
        input('\nPress ENTER to continue')

    @staticmethod
    def display_user_deleted(user):
        """
        Display information about deleted user
        :param user: User object
        :return:
        """
        print(ColorfulView.format_string_to_red('User: {} has been deleted'.format(user.get_login())))
        input('\nPress ENTER to continue')

    @staticmethod
    def get_value_to_change():
        """
        Get value to change mentor data
        :return:
        """
        return input('Enter what do you want to change('
                     + ColorfulView.format_string_to_green('login, phone, email, name') + '):')

    @staticmethod
    def display_user_not_found():
        """
        Display information that user is not found
        :return:
        """
        print(ColorfulView.format_string_to_red('User with that name not found!'))
        input('\nPress ENTER to continue ')

    @staticmethod
    def get_user_login():
        """
        Get login of the user
        :return:
        """
        return input('Enter login of the user: ')

    @staticmethod
    def get_new_role():
        """
        Get new role of the user
        :return:
        """
        return input('Choose new role: \033[91mS\033[0mtudent, \033[91mE\033[0mmployee, '
                     '\033[91mM\033[0mentor, \033[91mMan\033[0mager ')

    @staticmethod
    def display_wrong_role():
        """
        Display information about wrong role
        :return:
        """
        print('There is no such role.')
        input('\nPress ENTER to continue ')

    @staticmethod
    def display_email_sent():
        """
        Display information that email has been sent
        :return:
        """
        print('Email has been sent to everyone!')
        input('\nPress ENTER to continue ')

    @staticmethod
    def get_message_input():
        """
        Get message to send to everyone
        :return:
        """
        return input('Enter message do you want to send to everyone in Canvas: ')
