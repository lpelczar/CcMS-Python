import os


class EmployeeView:
    @staticmethod
    def display_input_error():
        print('Wrong input!')

    @staticmethod
    def menu():
        return input('''
        Choose option:
        1. Show students
        2. Exit
        ''')

    @staticmethod
    def display_students_list(students_list):
        os.system('clear')
        for student in students_list:
            print('Index: ' + students_list.index(student) + ' Name: ' + student.get_name() + ' Group: ' + student.group
                  + '\n' + 'Phone number:' + student.get_phone_number() + ' Email: ' '\n' + student.get_email())
            input('Press enter to return')
