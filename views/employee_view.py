from views.colorful_view import ColorfulView
from texttable import Texttable
import os
STARTING_INDEX = 1


class EmployeeView:
    @staticmethod
    def display_input_error():
        print(ColorfulView.format_string_to_red('Wrong input!'))

    @staticmethod
    def display_menu(name_of_user):
        welcome = ColorfulView.format_string_to_yellow('\tWelcome {}, this is your account options.\n'.format(name_of_user))
        title = ColorfulView.format_string_to_blue('\nChoose option:\n')
        options = '\n1. Show students\n2. Exit'

        print(welcome, title, options)

        return input()

    @staticmethod
    def display_students_list(students_list):
        os.system('clear')
        EmployeeView.print_table(students_list)
        input('\nPress ENTER to return')

    @staticmethod
    def display_chose_user_to_promote(users):
        os.system('clear')
        index = 1

        for person in users:
            print(str(index) + '.' + person)
            index += 1

        get_user_index = input('Enter user index to promote: ')
        return get_user_index

    @staticmethod
    def print_table(users):
        t = Texttable()
        t.set_cols_dtype(['a', 'a', 'a', 'a', 'i', 'a'])
        t.add_rows([['Index', 'Login', 'Name', 'Group', 'Phone Number', 'E-mail']] +
                   [[i + STARTING_INDEX, u.get_login(), u.get_name(), 'Not assigned' if not u.group else u.group,
                     u.get_phone_number(), u.get_email()] for i, u in enumerate(users)])
        print(t.draw())
