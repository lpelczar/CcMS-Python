import os

INDEX_INCREMENTOR = 1


class StudentView:
    @staticmethod
    def display_student_grades(grades_list: dict):
        if not grades_list:
            print('You have no added grades !')
        print('Assignments with grades:')
        for key, value in grades_list.items():
            print('Assignment name: {}; Grade: {}'.format(key, value))

    @staticmethod
    def display_submission_result():
        print('You successfully added new submission !')

    @staticmethod
    def display_user_assignments(assignments: list):
        os.system('clear')
        print('Assignments without your submission: ')

        for id, assignment in enumerate(assignments):
            print(str(id) + '. ' + assignment)

    @staticmethod
    def display_user_grades(assignments: list):
        os.system('clear')
        print('Your grades:')
        for id, assignment in enumerate(assignments):
            id += INDEX_INCREMENTOR
            print(str(id) + '. ' + assignment)

        input('\nPress ENTER to continue')

    @staticmethod
    def display_user_assignments(assignments: list):
        os.system('clear')
        print('Your assignments: ')

        for id, assignment in enumerate(assignments):
            print(str(id) + '. ' + assignment)

    @staticmethod
    def display_student_menu(user_login, role):
        greeting_message = 'Logged as {} ({}) \n'.format(user_login, role)
        print(greeting_message,
              '\n1. Submit submission'
              '\n2. View grades'
              '\n3. Exit system')

    @staticmethod
    def get_user_input(prompt: str):
        return input(prompt)

    @staticmethod
    def print_user_assignments_list_empty_error():
        os.system('clear')
        print('Your assignments list is empty !')
        input('\nPress ENTER to continue')

    @staticmethod
    def print_user_have_no_grades():
        os.system('clear')
        print('You have no added grades !')
        input('\nPress ENTER to continue')

    @staticmethod
    def print_wrong_assignment_id_error():
        os.system('clear')
        print('Assignment with this ID does not exist !')
        input('\nPress ENTER to continue')
