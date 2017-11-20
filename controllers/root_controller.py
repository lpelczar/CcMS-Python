from controllers.mentor_controller import MentorController
from controllers.manager_controller import ManagerController
from controllers.employee_controller import EmployeeController
from controllers.student_controller import StudentController
from views.root_view import RootView
from models.user_container import UserContainer
from models.user import User
from models.student import Student
from models.mentor import Mentor
from models.manager import Manager
from models.employee import Employee
from controllers.key_getch import getch
import os


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

            elif option == '0':
                UserContainer.get_instance().save_users_to_file()
                exit_program = False

    def handle_sign_up(self):
        """
        Handle creating new User
        """
        RootView.display_sign_menu(True)

        sing_up = True
        while sing_up:
            login = RootView.create_user_login()
            password = RootView.create_user_password()

            if self.user_container.get_user(login, password):
                RootView.display_user_already_exists()

            else:
                phone_number = RootView.create_user_phone_number()
                email = RootView.create_user_email()
                name = RootView.add_user_name()

                self.user_container.add_user(User(login, password, phone_number, email, name))
                RootView.display_user_created(login, password, phone_number, email, name)

                sing_up = False

    def handle_sign_in(self):
        """
        Handle logging to existing user
        """
        RootView.display_sign_menu(False)

        sing_in = True
        while sing_in:
            login, password = RootView.get_user_login_password()
            user = self.user_container.get_user(login, password)

            if user:

                if isinstance(user, Student):
                    StudentController(user).start()
                    sing_in = False

                elif isinstance(user, Mentor):
                    MentorController().start()
                    sing_in = False

                elif isinstance(user, Manager):
                    ManagerController(user).start()
                    sing_in = False

                elif isinstance(user, Employee):
                    EmployeeController().start()
                    sing_in = False

                elif isinstance(user, User):
                    RootView.display_error_user_singin()
                    sing_in = False
            else:
                RootView.display_user_not_exist()
