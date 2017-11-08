import os
from models.student import Student
from models.user_container import UserContainer
from views.student_view import StudentView


class StudentController:

    INSTANCE = None

    def __init__(self, student:Student):
        if self.INSTANCE is not None:
            raise ValueError("An instantiation already exists!")
        self.user_container = UserContainer.get_instance()
        self.student = student

    def start(self):
        should_exit = False
        while not should_exit:
            try:
                os.system('clear')
                StudentView.display_student_menu()
                user_input = StudentView.get_user_input('Choose an option: ')
                if user_input == '1':
                    self.submit_assignment()
                    StudentView.display_submission_result()
                elif user_input == '2':
                    self.show_student_grades()
            except Exception as e:
                print(e)


    @classmethod
    def get_instance(cls, student:Student):
        """
        Returns the singleton instance of Controller
        :return: None
        """
        if cls.INSTANCE is None:
            cls.INSTANCE = StudentController(student)
        return cls.INSTANCE

    def show_student_grades(self):
        """
        Show grades for student with given student login
        """
        if not self.student.assignments:
            StudentView.print_user_have_no_grades()

    def submit_assignment(self):
        """
        Add new key to submissions with assignment_name
        """
        assignment_without_submission = [assignment for assignment in self.student.assignments if assignment.submission == None]
        if not assignment_without_submission:
            StudentView.print_user_assignments_list_empty_error()
            return
        assignments_as_strings_list = [str(assignment) for assignment in assignment_without_submission]
        StudentView.display_user_assignments(assignments_as_strings_list)
        submission_id = int(StudentView.get_user_input('Type submission ID: '))
        submission_content = StudentView.get_user_input('Type link to github repository: ')
        self.student.add_submission(submission_id, submission_content)
