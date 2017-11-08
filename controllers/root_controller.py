from mentor_controller import MentorController
from manager_controller import ManagerController
from employee_controller import EmployeeController
from student_controller import StudentController


class RootController:

    INSTANCE = None

    def __init__(self):
        self.mentor_controller = MentorController()
        self.manager_controller = ManagerController()
        self.employee_controller = EmployeeController()
        self.student_controller = StudentController()

    @classmethod
    def get_instance(cls):
        """
        Returns the singleton instance of Controller
        :return: None
        """
        if cls.INSTANCE is None:
            cls.INSTANCE = RootController()
        return cls.INSTANCE
