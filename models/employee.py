from user import User


class Employee(User):

    def __init__(self, *args, **kwargs):
        super(Employee, self).__init__(*args, **kwargs)
