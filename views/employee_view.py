from colorful_view import ColorfulView
import os


class EmployeeView:
    @staticmethod
    def display_input_error():
        print(ColorfulView.format_string_to_red('Wrong input!'))

    @staticmethod
    def display_menu():
        menu = ColorfulView.format_string_to_yellow('''
        Choose option:
        1. Show students
        2. Exit
        ''')
        return input(menu)

    @staticmethod
    def display_students_list(students_list):
        os.system('clear')
        for student in students_list:
            if not student.group:
                group_str = ColorfulView.format_string_to_red('Not assigned')
            else:
                group_str = student.group
            print(ColorfulView.format_string_to_green('Index: ' + str(students_list.index(student)) + ' Name: ' + student.get_name() + ' Group: ' +
                  group_str + '\n' + 'Phone number:' + str(student.get_phone_number()) + ' Email: ' + '\n'
                  + student.get_email()))
        input('Press enter to return')
