from views.colorful_view import ColorfulView
import os
from datetime import date
from models.group_container import GroupContainer


class MentorView:
    @staticmethod
    def display_date_error():
        """
        Prints out date error

        :return: None
        """
        print(ColorfulView.format_string_to_red('Wrong date format!'))
        input('Press enter to return')

    @staticmethod
    def display_index_error():
        """
        Prints out display error

        :return: None
        """
        print(ColorfulView.format_string_to_red('Wrong index!'))
        input('Press enter to return')

    @staticmethod
    def show_invalid_input():
        """
        Prints out input error

        :return: None
        """
        print(ColorfulView.format_string_to_red('Invalid input!'))
        input('Press enter to return')

    @staticmethod
    def display_menu():
        """
        Prints out main menu of mentor controller and lets user choose an option

        :return: string -> chosen option
        """
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
8.Add group
9.Rename group
0.Exit""")
        return option

    @staticmethod
    def display_not_enough_data():
        """
        Prints out not enough data error message

        :return: None
        """
        print(ColorfulView.format_string_to_red('You have no students/groups/assignments added'))

    @staticmethod
    def display_assignments(assignments):
        """
        Prints out current assignments

        :param assignments: list -> list of assignments
        :return: None
        """
        os.system('clear')
        for assignment in assignments:
            print('Index: ' + str(assignments.index(assignment)) + ' Title: ' + assignment.title + '\n'
                  + assignment.description + '\n')
        input('Press enter to return')

    @staticmethod
    def display_students_list(students_list):
        """
        Prints out current students from list

        :param students_list: list -> list of current students
        :return: None
        """
        if not students_list:
            print(ColorfulView.format_string_to_red('No students found!'))
            return
        os.system('clear')
        for student in students_list:
            group_str = GroupContainer.get_instance().get_student_group_name(student)
            if not group_str:
                group_str = "Not assigned"
            print('Index: ' + str(students_list.index(student)) + ' Name: ' + student.name + ' Group: ' + group_str)
        input('Press enter to return')

    @staticmethod
    def display_student_assignments(student):
        """
        Display assignments data of certain student

        :param student: Student() -> student class object which holds its own assigments values
        :return: None
        """
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
        """
        Gets new assigments value for assigment creation

        :return: datetime(), str, str -> values necessary for creating assignment
        """
        os.system('clear')
        deadline = input('Type in deadline for assignment yyyy-mm-dd: ')
        deadline_list = deadline.split('-')
        deadline = date(int(deadline_list[0]), int(deadline_list[1]), int(deadline_list[2]))
        title = input('Type in title of the assignment: ')
        description = input('Describe your assignment: ')
        return deadline, title, description

    @staticmethod
    def get_student_index(students_list):
        """
        Gets student index from mentor, shows students list if needed

        :param students_list: list -> list of current students
        :return: str -> index of student
        """
        while True:
            os.system('clear')
            student_index = input("Type in student's index or s to show list of current students (with indexes): ")
            if student_index == 's':
                MentorView.display_students_list(students_list)
                continue
            return student_index

    @staticmethod
    def get_grade_values(student):
        """
        Gets index of assignment, shows student assignments with indexes if needed

        :param student: Student() -> student class object which holds its own assigments values
        :return: str, int -> values for grading assignment
        """
        while True:
            assignment_index = input("Type in assignment's index or s to show" +
                                     "list of current assignments (with indexes):")
            assignment_index = int(assignment_index)
            if assignment_index == 's':
                MentorView.display_student_assignments(student)
                continue
            break
        grade = input("Type in grade: ")
        return assignment_index, grade

    @staticmethod
    def get_presence(student):
        """
        Checks students presence

        :param student: Student() ->  Object for grading
        :return: bool -> True if student present, False otherwise
        """
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
        """
        Let's user choose value to change

        :return: str -> number of chosen option
        """
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
        """
        Prints out value you want to chenge and gets input of new value to assign

        :param string -> value name
        :return: str -> new value
        """
        return input('Type in new ' + string)

    @staticmethod
    def get_additional_attendance():
        """
        Gets value for increasing student's attendance

        :return: str -> number of days which will be added to attendance
        """
        os.system('clear')
        additional_days = input("How many days would you like to add to student's presence?")
        return additional_days

    @staticmethod
    def get_user_index(users):
        """
        Asks for  index of user

        :param users:list -> list of current users
        :return: str -> index of user
        """
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
        """
        Asks for group index

        :param group_list:list -> list of currently existing groups
        :return: str -> index of wanted group
        """
        MentorView.display_groups(group_list)
        group_index = input('Choose group: ')
        return group_index

    @staticmethod
    def display_groups(group_list, exit_with_enter=False):
        """
        Displays groups

        :param group_list:list -> list of current groups
        :param exit_with_enter:bool -> decides if methode should wait for input at the end
        :return: None
        """
        os.system('clear')
        print(ColorfulView.format_string_to_yellow('Current groups: '))
        for group in group_list:
            print(str(group_list.index(group)) + group.name)
        if exit_with_enter:
            input('Press enter to return')

    @staticmethod
    def get_group_name():
        """
        Asks for new group name

        :return: str -> new name of the group
        """
        return input('Type in group name: ')

    @staticmethod
    def display_group_exists():
        """
        Prints out message

        :return: None
        """
        print('Group with that name already exists!')
        input('Press enter to return')
