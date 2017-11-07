from user import User


class Employee(User):

    def __init__(self, *args, **kwargs):
        super(Employee, self).__init__(*args, **kwargs)

    def get_students():
        """
        :return: list of string representations of students
        """
        users = UserContainer.get_instance.get_users_list()
        return [str(person) for person in users if isinstance(person, Student)]
