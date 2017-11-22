from models.user_container import UserContainer


class Group:

    def __init__(self, name: str):
        self.student_login_list = []
        self.name = name
        self.attendance_check_count = 0

    def get_student_list(self):
        """
        Method returns list of student instances that belongs to this group
        :return: list -> list of student instances
        """
        student_instances = []
        for login in self.student_login_list:
            student = UserContainer.get_instance().get_user_by_login_or_email(login)
            student_instances.append(student)
        return student_instances
