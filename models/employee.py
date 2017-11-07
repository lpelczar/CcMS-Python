from user import User


class Employee(User):

    def __init__(self, *args, **kwargs):
        super(Employee, self).__init__(*args, **kwargs)

    def show_students():
        """
        :return: list of Students
        """
        users = UserContainer.get_users_list()
        return [person for person in users if isinstance(person, Student)]
