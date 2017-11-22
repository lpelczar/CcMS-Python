from views.colorful_view import ColorfulView
import os


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

        for student in students_list:

            if not student.group:
                group_str = ColorfulView.format_string_to_red('Not assigned')

            else:
                group_str = student.group

            print(ColorfulView.format_string_to_green('Index: ') + str(students_list.index(student))
                  + ColorfulView.format_string_to_green(' Name: ') + student.get_name() + '\nGroup: ' +
                  str(group_str) + '\nPhone number:' + str(student.get_phone_number()) + '\nEmail: '
                  + student.get_email())
        input('Press enter to return')

    @staticmethod
    def display_chose_user_to_promote(users):
        os.system('clear')
        index = 1

        for person in users:
            print(str(index) + '.' + person)
            index += 1

        get_user_index = input('Enter user index to promote: ')
        return get_user_index
