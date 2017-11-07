from mentor_controller import MentorController
from manager_controller import ManagerController
from employee_controller import EmployeeController
from student_controller import StudentController

class RootController:

    def __init__(self):
        self.mentor_controller = MentorController()
        self.manager_controller = ManagerController()
        self.employee_controller = EmployeeController()
        self.student_controller = StudentController()
