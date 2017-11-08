from controllers.mentor_controller import MentorController
from controllers.manager_controller import ManagerController
from controllers.employee_controller import EmployeeController
from controllers.student_controller import StudentController
from views.root_view import RootView
from models.user_container import UserContainer
from models.user import User
from controllers.key_getch import getch
import sys
import os


class RootController:

    INSTANCE = None

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
        while True:
            os.system('clear')
            RootView.display_starting_screen()
            RootView.display_main_menu()

            option = getch()  # Todo -> move input to RootView
            if option in self.OPTIONS.keys():
                if option == '1':
                    self.handle_sign_in()
                elif option == '2':
                    self.handle_sign_up()
                elif option == '0':
                    sys.exit()

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
                phone_number = RootView.create_user_phone_number()
                email = RootView.create_user_email()
                name = RootView.add_user_name()
                self.user_container.add_user(User(login, password, phone_number, email, name))
                RootView.display_user_created(login, password, phone_number, email, name)  # Todo -> in RootView 'User has been created!'
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
