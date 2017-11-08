from models.user_container import UserContainer
from views.employee_view import EmployeeView


class EmployeeController:

    def start(self):
        exit_program = False
        while not exit_program:
            option = EmployeeView.menu()
            if option == "1":
                self.show_students()
            elif option == "2":
                exit_program = True

    @staticmethod
    def show_students():
        students_list = UserContainer.get_students_list()
        EmployeeView.display_students_list(students_list)
