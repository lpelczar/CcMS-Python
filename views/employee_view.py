class EmployeeView:
    @staticmethod
    def menu():
        return input('''
        Choose option:
        1. Show students
        2. Exit
        ''')

    @staticmethod
    def display_students_list(students_list):
        for student in students_list:
            print(students_list.index(student) + student.get_name() + student.group + '\n' + student.get_phone_number()
                  + '\n' + student.get_email())
