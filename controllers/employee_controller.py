from models.user_container import UserContainer
from views.employee_view import EmployeeView
import os


class EmployeeController:

    def __init__(self):
        self.user_container = UserContainer.get_instance()

    def start(self, user):
        exit_program = False

        while not exit_program:
            os.system('clear')

            option = EmployeeView.display_menu(user.name)

            if option == "1":
                self.show_students()

            elif option == "2":
                user = self.show_users_to_promote()

                if self.is_student_already_exist(user):
                    EmployeeView.display_user_already_exist()

            elif option == "3":
                exit_program = True

            else:
                EmployeeView.display_input_error()
        self.user_container.get_instance().save_users_to_file()
        exit()

    def show_students(self):
        students_list = self.user_container.get_students_list()
        EmployeeView.display_students_list(students_list)

    def show_users_to_promote(self):
        users = self.user_container.get_users_with_user_range()
        get_user_account_index = EmployeeView.display_chose_user_to_promote(users)

        return get_user_account_index

    def is_student_already_exist(self, user):
        is_user_exist = self.user_container.get_user_by_login_or_email(user.login)
        if is_user_exist is None:
            return False
        else:
            return True
