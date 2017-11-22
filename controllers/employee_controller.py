from models.user_container import UserContainer
from models.student import Student
from services.notification_service import EmailService
from views.employee_view import EmployeeView
import os


class EmployeeController:

    def __init__(self, employee):
        self.user_container = UserContainer.get_instance()
        self.employee = employee

    def start(self):
        exit_program = False

        while not exit_program:
            os.system('clear')

            option = EmployeeView.display_menu(self.employee.name)

            if option == "1":
                self.show_students()

            elif option == "2":
                user = self.show_users_to_promote()

                if user is not None:
                    is_student_exist = self.is_student_already_exist(user)

                    if is_student_exist:
                        EmployeeView.display_user_already_exist()

                    else:
                        self.user_container.users.append(Student(user.login, user.password,
                                                         user.phone_number, user.email, user.name))
                        self.user_container.remove_user(user)

            elif option == "3":
                email_message = EmployeeView.ask_coffe_fundarising()

                if email_message is not None:
                    students_emails = self.get_students_emails()
                    for email in students_emails:
                        EmailService.send_email(email_message, email)


                else:
                    EmployeeView.display_emails_input_error()

            elif option == "0":
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
        if isinstance(user, Student):
            return True
        else:
            return False

    def get_students_emails(self):
        emails = [user.email for user in self.user_container if isinstance(user, Student)]
        return emails
