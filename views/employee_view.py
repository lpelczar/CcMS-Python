import os

from dependecies.texttable import Texttable
from views.colorful_view import ColorfulView

STARTING_INDEX = 1


class EmployeeView:
    @staticmethod
    def display_input_error():
        print(ColorfulView.format_string_to_red('Wrong input!'))

    @staticmethod
    def display_menu(name_of_user):
        welcome = ColorfulView.format_string_to_yellow('\tWelcome {}, this is your account options.\n'.format(name_of_user))
        title = ColorfulView.format_string_to_blue('\nChoose option:\n')
        options = '\n1. Show students\n2. Promote user to student\n3. Ask for send email about cofee fundarising\n0. Exit'

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
            print('\n' + str(index) + '. ' + ColorfulView.format_string_to_green(person.name) + ', Login: '
                  + ColorfulView.format_string_to_yellow(person.login) + ', Email: '
                  + ColorfulView.format_string_to_yellow(person.email))
            index += 1

        incorrect = True
        while incorrect:
            user_index = input('Enter user index to promote(or back): ')

            if user_index.isdigit():
                user = EmployeeView.get_user_by_index(user_index, users)
                return user

            elif user_index == 'back':
                incorrect = False

    @staticmethod
    def get_user_by_index(user_index, users):
        user_index = int(user_index)
        user_index -= 1
        return users[user_index]

    @staticmethod
    def display_user_already_exist():
        exist_info = ColorfulView.format_string_to_red('This user already exist as stundet!')
        print(exist_info)

    @staticmethod
    def ask_coffe_fundarising():
        send_emails = input('Would you like to send an email to stundents about coffe fundarising?(yes)\n')

        if send_emails.upper() == 'YES':
            message = 'Hello dear students!\nWe are going out off coffe in next few days!\n If you don\'t pay yet, '\
                      'please do this as soon as it possible! It\'s cost as always 123.5 pln!\nGreetings, \nyour Katarzyna!'

            print('Please wait for information about send emails!')
            return message

    @staticmethod
    def print_table(users):
        t = Texttable()
        t.set_cols_dtype(['a', 'a', 'a', 'a', 'i', 'a'])

        tittles = ['Index', 'Login', 'Name', 'Group', 'Phone Number', 'E-mail']
        tittles = [ColorfulView.format_string_to_green(i) for i in tittles]

        t.add_rows([tittles] + [[i + STARTING_INDEX, ColorfulView.format_string_to_yellow(u.get_login()), u.get_name(),
                   'Not assigned' if not u.group else u.group, u.get_phone_number(),
                   u.get_email()] for i, u in enumerate(users)])

        print(t.draw())

    @staticmethod
    def display_emails_input_error():
        print(ColorfulView.format_string_to_red('You type wrong input! Why you dont spam students by emails!'))
        input()

    @staticmethod
    def display_is_email_sent(email):
        email = ColorfulView.format_string_to_yellow(email)
        print(email + ColorfulView.format_string_to_green(' - email has been sent!'))
