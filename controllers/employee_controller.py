from models.user_container import UserContainer
from views.employee_view import EmployeeView
import os


class EmployeeController:

    def start(self, user):
        exit_program = False

        while not exit_program:
            os.system('clear')

            option = EmployeeView.display_menu(user.name)

            if option == "1":
                self.show_students()

            elif option == "2":
                exit_program = True

            else:
                EmployeeView.display_input_error()
        UserContainer.get_instance().save_users_to_file()
        exit()

    @staticmethod
    def show_students():
        students_list = UserContainer.get_instance().get_students_list()
        EmployeeView.display_students_list(students_list)
