import os


class MentorView:
    @staticmethod
    def date_error():
        print('Wrong date format!')
        input('Press enter to return')

    @staticmethod
    def display_index_error():
        print('Index out of range!')
        input('Press enter to return')

    @staticmethod
    def show_invalid_input():
        print('Invalid input!')
        input('Press enter to return')

    @staticmethod
    def menu():
        os.system('clear')
        options = ['1', '2', '3', '4', '5', '6', '7']
        option = ''
        while option not in options:
            option = input("""
Choose option:
1.Show students
2.Add assignment
3.Show assignments
4.Grade assignment
5.Check attendance
6.Change student    
7.Promote user to student 
8.Exit""")
        return option

    @staticmethod
    def display_assignments(assignments):
        os.system('clear')
        for assignment in assignments:
            print('Index: ' + str(assignments.index(assignment)) + ' Title: ' + assignment.title + '\n'
                  + assignment.description + '\n')

    @staticmethod
    def display_students_list(students_list):
        os.system('clear')
        for student in students_list:
            if student.group:
                group_str = student.group
            else:
                group_str = "Not assigned"
            print('Index: ' + str(students_list.index(student)) + ' Name: ' + student.name + ' Group: ' + group_str)

    @staticmethod
    def return_assignment_values():
        os.system('clear')
        deadline = input('Type in deadline for assignment yyyy-mm-dd: ')
        title = input('Type in title of the assignment: ')
        description = input('Describe your assignment: ')
        return deadline, title, description

    @staticmethod
    def get_grading_values():
        os.system('clear')
        student_index = int(input("Type in student's index: "))
        assignment_index = int(input("Type in assignment's index: "))
        grade = input("Type in grade: ")
        return student_index, assignment_index, grade

    @staticmethod
    def get_presence(student):
        os.system('clear')
        presence = None
        while presence != 'y' or presence != 'n':
            presence = input('Is ' +  student.get_name + ' present? (y/n)')
            if presence == 'y':
                return True
            if presence == 'n':
                return False

    @staticmethod
    def get_student_index():
        os.system('clear')
        while True:
            try:
                index = int(input("Type in student's index: "))
                return index
            except:
                print('Wrong index!')

    @staticmethod
    def get_group_name():
        return input('Type in group name: ')

    @staticmethod
    def student_value_to_change():
        os.system('clear')
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
            while True:
                try:
                    days = int(input('How many days would you like to add: '))
                    return days
                except:
                    print("Wrong value!")
        else:
            return input('Type in new ' + string)

    @staticmethod
    def get_user_to_assign(users):
        while True:
            if users:
                for user in users:
                    print('Index: ' + str(users.index(user)) + ' Name: ' + user.name + ' Email: ' + user.email)
                user_index = int(input('Type in index of user you want to assign to students: '))
                try:
                    user = users[user_index]
                    return user
                except:
                    print('Wrong index!')
            else:
                print("""
There are currently no unassigned users
                """)
                return
