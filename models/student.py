from user import User


class Student(User):

    def __init__(self, *args, **kwargs):
        self.submissions = {}  # Dictionary with key: Assignment name, value: grade
        self.group = None
        self.attendance = 0
        super(Student, self).__init__(*args, **kwargs)

    def get_grades(self):
        """
        :return: list -> list of grades
        """
        return list(self.submissions.values())
