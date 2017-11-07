from user import User


class Student(User):

    def __init__(self, *args, **kwargs):
        self.submissions = {}  # Dictionary with key: Assignment, value: Grade
        self.group = None
        self.attendance = 0
        super(Student, self).__init__(*args, **kwargs)

    def get_grades(self):
        """
        :return: list -> student grades
        """
        return list(self.submissions.values())

    def submit_assignment(self, assignment_name):
        """
        Add new key to submissions with assignment_name
        """
        self.submissions[assignment_name] = None
