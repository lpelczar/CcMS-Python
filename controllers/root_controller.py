from controllers.mentor_controller import MentorController
from controllers.manager_controller import ManagerController
from controllers.employee_controller import EmployeeController
from controllers.student_controller import StudentController
from views.root_view import RootView
from models.user_container import UserContainer
from models.user import User
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
        """
        Main loop for the program
        """
        RootView.display_starting_screen()
        RootView.display_main_menu()
        while True:
            option = RootView.get_option_input()
            os.system('clear')
            RootView.display_main_menu()
            if option in self.OPTIONS.keys():
                if option == '1':
                    self.handle_sign_in()
                elif option == '2':
                    self.handle_sign_up()

    def handle_sign_up(self):
        """
        Handle creating new User
        """
        RootView.display_sign_menu(True)
        while True:
            login = RootView.create_user_login()
            password = RootView.create_user_password()
            if self.user_container.get_user(login, password):
                RootView.display_user_already_exists()
                continue
            else:
                self.user_container.add_user(User(login, password))
                RootView.display_user_created()
                break

    def handle_sign_in(self):
        """
        Handle logging to existing user
        """
        RootView.display_sign_menu(False)
        while True:
            login, password = RootView.get_user_login_password()
            user = self.user_container.get_user(login, password)
            if user:
                if isinstance(User, Student):
            else:
                RootView.display_user_not_exist()
