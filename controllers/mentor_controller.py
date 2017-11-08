from models.user_container import UserContainer
from models.assignment import Assignment
from models.assignment_container import AssignmentContainer
from views.mentor_view import MentorView
from models.student import Student
from models.group import Group


class MentorController:
    def __init__(self):
        self.INSTANCE = None
        if self.INSTANCE is not None:
            raise ValueError("An instantiation already exists!")

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
        students_list = UserContainer.get_students_list()
        MentorView.display_students_list(students_list)

    @staticmethod
    def add_assignment():
        students_list = UserContainer.get_students_list()
        deadline, title, description = MentorView.display_add_assignment()
        new_assignment = Assignment(deadline, title, description)
        AssignmentContainer.get_instance().add_assignment(new_assignment)
        for student in students_list:
            student.add_student_assigment(deadline, title, description)

    @staticmethod
    def grade_assignment():
        #student_index, assignment_index, grade = MentorView.
        students_list = UserContainer.get_students_list()
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
        students_list = UserContainer.get_students_list()
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
