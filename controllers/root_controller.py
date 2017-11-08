from mentor_controller import MentorController
from manager_controller import ManagerController
from employee_controller import EmployeeController
from student_controller import StudentController
from root_view import RootView
from user_container import UserContainer
from user import User
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
        self.user_container = UserContainer.get_instance()

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
            option = input('Choose option: ')  # Todo -> move input to RootView
            os.system('clear')
            RootView.display_main_menu()
            if option in self.OPTIONS.keys():
                if option == '1':
                    self.handle_sign_in()
                elif option == '2':
                    self.handle_sign_up()

    def handle_sign_up(self):
        RootView.display_sing_menu(True)
        while True:
            login, password = RootView.display_sign_up_menu()
            if self.user_container.get_user(login, password):
                RootView.display_user_already_exists()  # Todo -> in RootView 'User already exists!'
                continue
            else:
                self.user_container.add_user(User(login, password))
                RootView.display_user_created()  # Todo -> in RootView 'User has been created!'
                break
