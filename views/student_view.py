import os

from dependencies.texttable import Texttable, get_color_string, bcolors
from views.colorful_view import ColorfulView

INDEX_INCREMENTOR = 1

MENU_OPTIONS = {'1': 'Submit submission',
                '2': 'View grades',
                '3': 'Exit system',}

COLORED_MENU_OPTIONS = {get_color_string(bcolors.PURPLE, k): get_color_string(bcolors.PURPLE, v)
                        for k, v in MENU_OPTIONS.items()}

class StudentView:
    @staticmethod
    def display_student_grades(grades_list: dict):
        if not grades_list:
            print(ColorfulView.format_string_to_blue('You have no added grades !'))
        print(ColorfulView.format_string_to_yellow('Assignments with grades:'))
        for key, value in grades_list.items():
            print('Assignment name: {}; Grade: {}'.format(key, value))

    @staticmethod
    def display_submission_result():
        print(ColorfulView.format_string_to_green('You successfully added new submission !'))

    @staticmethod
    def display_user_assignments(assignments: list):
        os.system('clear')
        print(ColorfulView.format_string_to_yellow('Assignments without your submission: '))

        for index, assignment in enumerate(assignments):
            print(str(index) + '. ' + assignment)

    @staticmethod
    def display_user_grades(assignments: list):
        os.system('clear')
        print(ColorfulView.format_string_to_green('Your grades:'))
        for index, assignment in enumerate(assignments):
            index += INDEX_INCREMENTOR
            print(ColorfulView.format_string_to_blue(str(index) + '. ') + assignment)

        input('\nPress ENTER to continue')

    @staticmethod
    def display_student_menu(user_login, role):
        greeting_message = get_color_string(bcolors.BLUE, 'Logged as {} ({})'.format(user_login, role))
        t = Texttable()
        t.set_deco(Texttable.HEADER)
        t.add_rows([['', greeting_message]] +
                   [[k, v] for k, v in COLORED_MENU_OPTIONS.items()])
        print(t.draw())

    @staticmethod
    def get_user_input(prompt: str):
        return input(prompt)

    @staticmethod
    def print_user_assignments_list_empty_error():
        os.system('clear')
        print(ColorfulView.format_string_to_green('Your assignments list is empty !'))
        input('\nPress ENTER to continue')

    @staticmethod
    def print_user_have_no_grades():
        os.system('clear')
        print(ColorfulView.format_string_to_yellow('You have no added grades !'))
        input('\nPress ENTER to continue')

    @staticmethod
    def print_wrong_assignment_id_error():
        os.system('clear')
        print(ColorfulView.format_string_to_red('Assignment with this ID does not exist !'))
        input('\nPress ENTER to continue')
