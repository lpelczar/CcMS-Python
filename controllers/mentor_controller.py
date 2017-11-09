from models.user_container import UserContainer
from models.assignment import Assignment
from models.assignment_container import AssignmentContainer
from views.mentor_view import MentorView
from models.group import Group
from models.student import Student


class MentorController:
    def __init__(self):
        self.INSTANCE = None
        if self.INSTANCE is not None:
            raise ValueError("An instantiation already exists!")

    def start(self):
        exit_program = False
        while not exit_program:
            option = MentorView.menu()
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
        new_assignment = Assignment(deadline, title, description)
        AssignmentContainer.get_instance().add_assignment(new_assignment)
        for student in students_list:
            student.add_student_assigment(deadline, title, description)

    @staticmethod
    def grade_assignment():
        student_index, assignment_index, grade = MentorView.get_grading_values()
        students_list = UserContainer.get_instance().get_students_list()
        students_list[student_index].assigments[assignment_index].grade = grade

    @staticmethod
    def check_attendance():
        group_name = MentorView.get_group_name()
        group = Group.get_students_by_group(group_name)
        for student in group:
            student_present = MentorView.get_presence(student)
            if student_present:
                student.attendance += 1
        group.attendance_check_count += 1

    @staticmethod
    def change_student_data():
        students_list = UserContainer.get_instance().get_students_list()
        student_index = MentorView.get_student_index()
        student = students_list[student_index]
        value_to_change = MentorView.student_value_to_change()
        if value_to_change == '1':
            student.login = MentorView.new_value('login')
        elif value_to_change == '2':
            student.name = MentorView.new_value('name')
        elif value_to_change == '3':
            student.password = MentorView.new_value('password')
        elif value_to_change == '4':
            student.attendance += MentorView.new_value('attendance')
        elif value_to_change == '5':
            student.group = MentorView.new_value('group')

    @staticmethod
    def promote_user_to_student():
        not_assigned_users = UserContainer.get_instance().get_not_assigned_users_list()
        user_to_assign = MentorView.get_user_to_assign(not_assigned_users)
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


