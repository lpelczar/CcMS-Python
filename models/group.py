from models.user_container import UserContainer


class Group:

    def __init__(self, name: str):
        self.__student_login_list = []
        self.name = name

    def get_student_list(self):
        """
        Method returns list of student instances that belongs to this group
        :return: list -> list of student instances
        """
        student_instances = []
        for login in self.__student_login_list:
            student = UserContainer.get_instance().get_user_by_login(login)
            student_instances.append(student)
