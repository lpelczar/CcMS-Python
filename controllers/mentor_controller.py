from models.user_container import UserContainer
from models.assignment import Assignment
from models.assignment_container import AssignmentContainer
from views.mentor_view import MentorView
from models.group import Group
from models.student import Student
from datetime import date


class MentorController:
    def __init__(self):
        self.INSTANCE = None
        if self.INSTANCE is not None:
            raise ValueError("An instantiation already exists!")

    def start(self):
        exit_program = False
        while not exit_program:
            option = MentorView.display_menu()
            if option == '1':
                self.show_students()
            elif option == '2':
                self.add_assignment()
            elif option == '3':
                self.show_assignments()
            elif option == '4':
                self.grade_assignment()
            elif option == '5':
                self.check_attendance()
            elif option == '6':
                self.change_student_data()
            elif option == '7':
                self.promote_user_to_student()
            elif option == '8':
                exit_program = True
            else:
                MentorView.show_invalid_input()
        exit()

    @classmethod
    def get_instance(cls):
        """
        Returns the singleton instance of Controller
        :return: None
        """
        if cls.INSTANCE is None:
            cls.INSTANCE = MentorController()
        return cls.INSTANCE

    @staticmethod
    def show_students():
        students_list = UserContainer.get_instance().get_students_list()
        MentorView.display_students_list(students_list)

    @staticmethod
    def show_assignments():
        assignments = AssignmentContainer.get_instance().get_assignments_list()
        MentorView.display_assignments(assignments)

    @staticmethod
    def add_assignment():
        students_list = UserContainer.get_instance().get_students_list()
        deadline, title, description = MentorView.return_assignment_values()
        try:
            deadline_list = deadline.split('-')
            deadline = date(int(deadline_list[0]), int(deadline_list[1]), int(deadline_list[2]))
        except:
            MentorView.display_date_error()
            return
        new_assignment = Assignment(deadline, title, description)
        AssignmentContainer.get_instance().add_assignment(new_assignment)
        for student in students_list:
            student.add_student_assignment(deadline, title, description)

    @staticmethod
    def grade_assignment():
        students_list = UserContainer.get_instance().get_students_list()
        if not students_list:
            MentorView.display_not_enough_data()
            return
        student_index = MentorView.get_student_index(students_list)
        try:
            student_index = int(student_index)
            if not students_list[student_index].assignments:
                MentorView.display_not_enough_data()
                return
            student = students_list[student_index]
            assignment_index, grade = MentorView.get_grade_values(student)
            assignment_index = int(assignment_index)
        except:
            MentorView.show_invalid_input()
            return
        students_list = UserContainer.get_instance().get_students_list()
        try:
            students_list[student_index].assignments[assignment_index].grade = grade
        except:
            MentorView.display_index_error()
            return

    @staticmethod
    def check_attendance():
        groups = Group.groups_list
        if groups:
            group_index = MentorView.get_group_index(groups)
            try:
                group_index = int(group_index)
                group = groups[group_index]
            except:
                MentorView.display_index_error()
                return
        else:
            return
        group_students = Group.get_students_by_group(group.name)
        for student in group_students:
            student_present = MentorView.get_presence(student)
            if student_present:
                student.attendance += 1
        group.attendance_check_count += 1

    @staticmethod
    def change_student_data():
        value_changing = True
        students_list = UserContainer.get_instance().get_students_list()
        if not students_list:
            MentorView.display_not_enough_data()
            return
        student_index = MentorView.get_student_index(students_list)
        try:
            student_index = int(student_index)
            student = students_list[student_index]
        except IndexError:
            MentorView.display_index_error()
            return
        while value_changing:
            value_to_change = MentorView.get_student_value_to_change()
            if value_to_change == '1':
                student.login = MentorView.get_new_value('login')
            elif value_to_change == '2':
                student.name = MentorView.get_new_value('name')
            elif value_to_change == '3':
                student.password = MentorView.get_new_value('password')
            elif value_to_change == '4':
                additional_days = MentorView.get_additional_attendance()
                try:
                    student.attendance += int(additional_days)
                except:
                    MentorView.show_invalid_input()
            elif value_to_change == '5':
                student.group = MentorView.get_new_value('group')
            elif value_to_change == '6':
                return
            else:
                MentorView.show_invalid_input()

    @staticmethod
    def promote_user_to_student():
        not_assigned_users = UserContainer.get_instance().get_not_assigned_users_list()
        user_index = MentorView.get_user_index(not_assigned_users)
        try:
            user_index = int(user_index)
            user_to_assign = not_assigned_users[user_index]
        except:
            MentorView.display_index_error()
            return
        name = user_to_assign.name
        login = user_to_assign.login
        password = user_to_assign.password
        phone_number = user_to_assign.phone_number
        email = user_to_assign.email
        UserContainer.get_instance().remove_user(user_to_assign)
        if not user_to_assign:
            return
        user_to_assign = Student(name, login, password, phone_number, email)
        UserContainer.get_instance().add_user(user_to_assign)


