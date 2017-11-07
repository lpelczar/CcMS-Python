from user import User


class Student(User):

    def __init__(self, *args, **kwargs):
        self.submissions = {}  # Dictionary with key: Assignment name, value: Assignment Submission
        self.grades = []  # List of student grades
        self.group = None
        self.attendance = 0
        super(Student, self).__init__(*args, **kwargs)

    def get_grades(self):
        """
        :return: list -> student grades
        """
        return self.grades

    def submit_assignment(self, assignment_name):
        """
        Add new key to submissions with assignment_name
        """
        self.submissions[assignment_name] = StudentController.submission_input()

    def get_submissions(self):
        """
        :return: dict -> student submissions
        """
        return self.submissions
