from views.colorful_view import ColorfulView
from texttable import Texttable
import os

STARTING_INDEX = 1


class ManagerView:

    @staticmethod
    def display_manager_menu(user_login, role):
        greeting_message = ColorfulView.format_string_to_yellow('Logged as {} ({}) \n'.format(user_login, role))
        print(ColorfulView.format_string_to_green(greeting_message) +
              '1. Promote user to Mentor\n' +
              '2. Remove Mentor\n' +
              '3. Edit Mentor data\n' +
              '4. Display list of Mentors\n' +
              '5. Display list of Students\n'
              '6. Exit manager')

    @staticmethod
    def get_user_input(prompt: str):
        return input(prompt)

    @staticmethod
    def display_actual_list(users):
        print('')
        ManagerView.print_table(users)
        print('')

    @staticmethod
    def print_table(users):
        t = Texttable()
        t.add_rows([['Index', 'Login', 'Name', 'Role', 'Phone Number', 'E-mail']] +
                   [[i + STARTING_INDEX, u.get_login(), u.get_name(), u.__class__.__name__, u.get_phone_number(),
                     u.get_email()] for i, u in enumerate(users)])
        print(t.draw())

    @staticmethod
    def display_empty_list_message():
        print('')
        print(ColorfulView.format_string_to_red('List is empty!'))
        input('\nPress ENTER to continue')

    @staticmethod
    def display_users(users):
        print('')
        ManagerView.print_table(users)
        input('\nPress ENTER to continue')

    @staticmethod
    def display_mentor_information(mentor_data):
        os.system('clear')
        print(ColorfulView.format_string_to_yellow('Name: ') + mentor_data.get_name()
              + ColorfulView.format_string_to_green('\nLogin: ') + mentor_data.get_login()
              + ColorfulView.format_string_to_green('\nPhone number: ') + mentor_data.get_phone_number()
              + ColorfulView.format_string_to_green('\nEmail: ') + mentor_data.get_email())

    @staticmethod
    def get_promotion_input():
        return input('Enter login of the user which do you want to promote to Mentor: ')

    @staticmethod
    def get_user_remove_input():
        return input('Enter login of the user which do you want to remove: ')

    @staticmethod
    def get_user_edit_input():
        return input('Enter login of the mentor which do you want to modify: ')

    @staticmethod
    def get_new_value():
        return input('Enter new value: ')

    @staticmethod
    def display_wrong_attribute():
        print(ColorfulView.format_string_to_red('There is no such attribute to change!'))
        input('\nPress ENTER to continue')

    @staticmethod
    def display_user_promoted(user):
        print(ColorfulView.format_string_to_green('User: {} has been promoted to Mentor'.format(user.get_login())))
        input('\nPress ENTER to continue')

    @staticmethod
    def display_user_deleted(user):
        print(ColorfulView.format_string_to_red('User: {} has been deleted'.format(user.get_login())))
        input('\nPress ENTER to continue')

    @staticmethod
    def get_value_to_change():
        return input('Enter what do you want to change('
                     + ColorfulView.format_string_to_green('login, phone, email, name') + '):')

    @staticmethod
    def display_user_not_found():
        print(ColorfulView.format_string_to_red('User with that name not found!'))
        input('\nPress ENTER to continue')
