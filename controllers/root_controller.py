from mentor_controller import MentorController
from manager_controller import ManagerController
from employee_controller import EmployeeController
from student_controller import StudentController
from root_view import RootView
import os


class RootController:

    INSTANCE = None

    OPTIONS = OPTIONS = {'1': 'Sign in',
                         '2': 'Sign up'}

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

    def start(self):
        RootView.display_starting_screen()
        while True:
            option = input('Choose option: ')  #Todo -> move input to RootView
            os.system('clear')
            RootView.display_main_menu()
            if option in self.OPTIONS.keys():
                if option == '1':
                    self.add_todo_item()
                elif option == '2':
                    self.modify_item()
                elif option == '3':
                    self.delete_item()
                elif option == '4':
                    self.mark_as_done()
                elif option == '5':
                    self.display_items()
