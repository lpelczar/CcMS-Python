from models.user_container import UserContainer
from models.assignment import Assignment
from models.assignment_container import AssignmentContainer
from views.mentor_view import MentorView
from models.student import Student


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
        students_list = [user for user in UserContainer.get_instance().get_users_list() if isinstance(user, Student)]
        MentorView.display_students_list(students_list)

    @staticmethod
    def add_assignment():
        deadline, title, description = MentorView.display_add_assignment()
        new_assignment = Assignment(deadline, title, description)
        AssignmentContainer.add_assignment(new_assignment)

    def grade_assignment(self, student_index, assignment_index):
        pass

    def check_attendance(self):
        pass

    def promote_user_to_student(self):
        pass

    def change_student_data(self):
        pass

