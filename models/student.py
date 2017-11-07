from user import User


class Student(User):

    def __init__(self, *args, **kwargs):
        self.submissions = {}
        self.group = None
        self.attendance = 0
        super(Student, self).__init__(*args, **kwargs)
