import os

from controllers.employee_controller import EmployeeController
from controllers.key_getch import getch
from controllers.manager_controller import ManagerController
from controllers.mentor_controller import MentorController
from controllers.recovery_controller import RecoveryController
from controllers.student_controller import StudentController
from models.employee import Employee
from models.manager import Manager
from models.mentor import Mentor
from models.student import Student
from models.user import User
from models.user_container import UserContainer
from services.password_service import PasswordService
from views.root_view import RootView


class RootController:

    def __init__(self):
        self.user_container = UserContainer.get_instance()

    def start(self):
        """
        Main loop for the program
        """
        exit_program = True
        RootView.display_animate_starting_screen()

        while exit_program:
            os.system('clear')

            RootView.display_main_menu_screen()
            RootView.display_main_menu()
            option = getch()

            if option == '1':
                self.handle_sign_in()

            elif option == '2':
                self.handle_sign_up()
            elif option == '3':
                RecoveryController().start()
            elif option == '0':
                UserContainer.get_instance().save_users_to_file()
                exit_program = False

    def handle_sign_up(self):
        """
        Handle creating new User
        """
        RootView.display_sign_menu(True)

        user_created = False
        while not user_created:

            login = RootView.create_user_login()
            password = RootView.create_user_password()
            hashed_password = PasswordService.encrypt_password(password)

            if self.user_container.get_user_by_login_or_email(login):
                RootView.display_user_already_exists()

            else:
                phone_number = RootView.create_user_phone_number()
                email = RootView.create_user_email()
                name = RootView.add_user_name()

                self.user_container.add_user(User(login, hashed_password, phone_number, email, name))
                RootView.display_user_created(login, phone_number, email, name)
                user_created = True

    def handle_sign_in(self):
        """
        Handle logging to existing user
        """
        RootView.display_sign_menu(False)

        logged_in = False
        while not logged_in:

            login, password = RootView.get_user_login_password()
            password = PasswordService.encrypt_password(password)
            user = self.user_container.get_user(login, password)

            if user:

                logged_in = True
                if isinstance(user, Student):
                    StudentController(user).start()
                elif isinstance(user, Mentor):
                    MentorController().start()
                elif isinstance(user, Manager):
                    ManagerController(user).start()
                elif isinstance(user, Employee):
                    EmployeeController().start()
                elif isinstance(user, User):
                    RootView.display_error_user_singin()

            else:
                RootView.display_user_not_exist()
