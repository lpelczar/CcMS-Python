import traceback
from models.student import Student
from models.user_container import UserContainer
from views.student_view import StudentView


class StudentController:

    def __init__(self, student:Student):
        if self.INSTANCE is not None:
            raise ValueError("An instantiation already exists!")
        self.user_container = UserContainer.get_instance()
        self.student = student

    def start(self):
        should_exit = False
        while not should_exit:
            try:
                StudentView.display_student_menu()
                user_input = StudentView.get_user_input('Choose an option')
            except Exception as e:
                print(e)


    @classmethod
    def get_instance(cls):
        """
        Returns the singleton instance of Controller
        :return: None
        """
        if cls.INSTANCE is None:
            cls.INSTANCE = StudentController()
        return cls.INSTANCE

    def show_student_grades(self, student_login):
        """
        Show grades for student with given student login
        """
        students = self.user_container.get_students_list()
        for pupil in students:
            if pupil.get_login() == student_login:
                assignments_with_grades = pupil.get_grades()
                StudentView.display_student_grades(assignments_with_grades)
                return
        else:
            raise ValueError('No student with this login!')

    def submit_assignment(self, student_login, assignment_name):
        """
        Add new key to submissions with assignment_name
        """
        students = self.user_container.get_students_list()
        for pupil in students:
            if pupil.get_login() == student_login:
                pupil.submissions[assignment_name] = self.get_submission_input(assignment_name)
                StudentView.display_submission_result()
                return
        else:
            raise ValueError('No student with this login!')

    @staticmethod
    def get_submission_input(assignment_name):
        submission = input('Assignment: {} Enter link with your submission: '.format(assignment_name))
        return submission
