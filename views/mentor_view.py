from colorful_view import ColorfulView
import os


class MentorView:
    @staticmethod
    def display_date_error():
        print(ColorfulView.format_string_to_red('Wrong date format!'))
        input('Press enter to return')

    @staticmethod
    def display_index_error():
        print(ColorfulView.format_string_to_red('Wrong index!'))
        input('Press enter to return')

    @staticmethod
    def show_invalid_input():
        print(ColorfulView.format_string_to_red('Invalid input!'))
        input('Press enter to return')

    @staticmethod
    def display_menu():
        options = ['1', '2', '3', '4', '5', '6', '7', '8']
        option = ''
        while option not in options:
            os.system('clear')
            option = input("""
Choose option:
1.Show students
2.Add assignment
3.Show assignments
4.Grade assignment
5.Check attendance
6.Change student data
7.Promote user to student
8.Exit""")
        return option

    @staticmethod
    def display_not_enough_data():
        print(ColorfulView.format_string_to_red('You have no students/groups/assignments added'))

    @staticmethod
    def display_assignments(assignments):
        os.system('clear')
        for assignment in assignments:
            print('Index: ' + str(assignments.index(assignment)) + ' Title: ' + assignment.title + '\n'
                  + assignment.description + '\n')
        input('Press enter to return')

    @staticmethod
    def display_students_list(students_list):
        if not students_list:
            print(ColorfulView.format_string_to_red('No students found!'))
            return
        os.system('clear')
        for student in students_list:
            if student.group:
                group_str = student.group.name
            else:
                group_str = "Not assigned"
            print('Index: ' + str(students_list.index(student)) + ' Name: ' + student.name + ' Group: ' + group_str)
        input('Press enter to return')

    @staticmethod
    def display_student_assignments(student):
        print(student.name + "'s assignments:")
        for assignment in student.assignments:
            if not assignment.grade:
                grade_str = 'Not graded yet'
            else:
                grade_str = assignment.grade
            if not assignment.submission:
                assignment_str = 'No submission'
            else:
                assignment_str = assignment.submission
            print('Title: ' + assignment.title + '\nSubmission: ' + assignment_str + '\nGrade:' +
                  grade_str + '\n\n ')
        input('Press enter to return')

    @staticmethod
    def return_assignment_values():
        os.system('clear')
        deadline = input('Type in deadline for assignment yyyy-mm-dd: ')
        title = input('Type in title of the assignment: ')
        description = input('Describe your assignment: ')
        return deadline, title, description

    @staticmethod
    def get_student_index(students_list):
        while True:
            os.system('clear')
            student_index = input("Type in student's index or s to show list of current students (with indexes): ")
            if student_index == 's':
                MentorView.display_students_list(students_list)
                continue
            return student_index

    @staticmethod
    def get_grade_values(student):
        while True:
            assignment_index = input("Type in assignment's index or s to show "
                                     "list of current assignments (with indexes): ")
            if assignment_index == 's':
                MentorView.display_student_assignments(student)
                continue
            break
        grade = input("Type in grade: ")
        return assignment_index, grade

    @staticmethod
    def get_presence(student):
        os.system('clear')
        presence = None
        while presence != 'y' or presence != 'n':
            presence = input('Is ' + student.name + ' present? (y/n)')
            if presence == 'y':
                return True
            if presence == 'n':
                return False
            else:
                print(ColorfulView.format_string_to_red('Invalid input!'))

    @staticmethod
    def get_student_value_to_change():
        os.system('clear')
        return input('''
Which value would you like to change:
1. Login
2. Name
3. Password
4. Attendance
5. Group

Type in 6 to return to main menu
''')

    @staticmethod
    def get_new_value(string):
        return input('Type in new ' + string)

    @staticmethod
    def get_additional_attendance():
        os.system('clear')
        additional_days = input("How many days would you like to add to student's presence?")
        return additional_days

    @staticmethod
    def get_user_index(users):
        os.system('clear')
        if users:
            for user in users:
                print('Index: ' + str(users.index(user)) + ' Name: ' + user.name + ' Email: ' + user.email)
            user_index = input('Type in index of user you want to assign to students: ')
            return user_index
        else:
            print("""
There are currently no unassigned users
                """)
            input('Press enter to return')

    @staticmethod
    def get_group_index(group_list):
        MentorView.display_groups(group_list)
        group_index = input('Choose group: ')
        return group_index

    @staticmethod
    def display_groups(group_list, exit_with_enter=False):
        os.system('clear')
        print('Current groups: ')
        for group in group_list:
            print(str(group_list.index(group)) + group.name)
        if exit_with_enter:
            input('Press enter to return')
