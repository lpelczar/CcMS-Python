import os
import traceback

from models.manager import Manager
from models.mentor import Mentor
from models.user_container import UserContainer
from views.manager_view import ManagerView
from views.root_view import RootView
import os


class ManagerController:

    def __init__(self, manager: Manager):
        self.user_container = UserContainer.get_instance()
        self.manager = manager

    def start(self):
        should_exit = False
        while not should_exit:
            os.system('clear')
            ManagerView.display_manager_menu(self.manager.login, 'Manager')
            user_input = ManagerView.get_user_input('Choose an option: ')
            if user_input == '1':
                self.promote_user_to_mentor()
            elif user_input == '2':
                self.remove_mentor()
            elif user_input == '3':
                self.edit_mentor_data()
            elif user_input == '4':
                self.display_mentors()
            elif user_input == '5':
                self.display_students()
            elif user_input == '6':
                should_exit = True
        UserContainer.get_instance().save_users_to_file()
        os.system('clear')

    def promote_user_to_mentor(self):
        """
        Make selected User a Mentor

        :return: None
        """
        users = self.user_container.get_users_with_user_range()
        is_empty = ManagerView.display_actual_list(users)

        if not is_empty:
            user_login = ManagerView.get_promotion_input()
            try:
                user = self.user_container.get_user_by_login(user_login)
                self.user_container.users.append(Mentor(user.get_login(), user.get_password(),
                                                        user.get_phone_number(), user.get_email(),
                                                        user.get_name()))
                self.user_container.remove_user(user)
                ManagerView.display_user_promoted(user)
            except AttributeError:
                ManagerView.display_user_not_found()

    def edit_mentor_data(self):
        """
        Modify selected mentor data: login, phone number, email, name
        """
        mentors = self.user_container.get_mentor_list()
        ManagerView.display_actual_list(mentors)
        is_empty = ManagerView.display_actual_list(users)

        if not is_empty:
            mentor_login = ManagerView.get_user_edit_input()

        try:
            user = self.user_container.get_user_by_login(mentor_login)
            ManagerView.display_mentor_information(user)
            value_to_change = ManagerView.get_value_to_change()

            if value_to_change == 'login':
                user.set_login(RootView.create_user_login())
            elif value_to_change == 'phone':
                user.set_phone_number(RootView.create_user_phone_number())
            elif value_to_change == 'email':
                user.set_email(RootView.create_user_email())
            elif value_to_change == 'name':
                user.set_name(RootView.add_user_name())
            else:
                ManagerView.display_wrong_attribute()
        except AttributeError:
            ManagerView.display_user_not_found()

    def remove_mentor(self):
        """
        Remove mentor from list and display appripriate message

        :return: None
        """
        mentors = self.user_container.get_mentor_list()
        ManagerView.display_actual_list(mentors)
        is_empty = ManagerView.display_actual_list(users)

        if not is_empty:
            user_login = ManagerView.get_user_remove_input()
        try:
            user = self.user_container.get_user_by_login_or_email(user_login)
            self.user_container.remove_user(user)
            ManagerView.display_user_deleted(user)
        except ValueError:
            ManagerView.display_user_not_found()
        except AttributeError:
            ManagerView.display_user_not_found()

    def display_students(self):
        """
        Display list of all students

        :return: None
        """
        students = self.user_container.get_students_list()
        ManagerView.display_users(students)

    def display_mentors(self):
        """
        Display list of all mentors

        :return: None
        """
        mentors = self.user_container.get_mentor_list()
        ManagerView.display_users(mentors)
