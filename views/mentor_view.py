class MentorView:

    @staticmethod
    def show_invalid_input():
        print('Invalid input!')

    @staticmethod
    def menu():
        options = ['1', '2', '3', '4', '5']
        option = ''
        while option not in options:
            option = input("""
            Choose option:
            1.Show students
            2.Add assignment
            3.Grade assignment
            4.Check attendance
            5.Change student data
            6.Exit""")
        return option

    @staticmethod
    def display_students_list(students_list):
        for student in students_list:
            print(students_list.index(student) + student.get_name() + student.group)

    @staticmethod
    def display_add_assignment():
        deadline = input('Type in deadline for assignment dd-mm-yyyy: ')
        title = input('Type in title of the assignment: ')
        description = input('Describe your assignment: ')
        return deadline, title, description

    @staticmethod
    def get_grading_values():
        student_index = int(input("Type in student's index: "))
        assignment_index = int(input("Type in assignment's index: "))
        grade = input("Type in grade: ")
        return student_index, assignment_index, grade

    @staticmethod
    def get_presence(student):
        presence = None
        while presence != 'y' or presence != 'n':
            presence = input('Is ' +  student.get_name + ' present? (y/n)')
            if presence == 'y':
                return True
            if presence == 'n':
                return False

    @staticmethod
    def get_student_index():
        return int(input("Type in student's index: "))

    @staticmethod
    def get_group_name():
        return input('Type in group name: ')

    @staticmethod
    def student_value_to_change():
        return input('''
        Which value would you like to change:
        1. Login
        2. Name
        3. Password
        4. Attendance
        5. Group''')

    @staticmethod
    def new_value(string):
        if string == 'attendance':
            return int(input('How many days would you like to add: '))
        else:
            return input('Type in new ' + string)
