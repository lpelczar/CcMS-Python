from models.user_container import UserContainer
from models.manager import Manager
from models.mentor import Mentor
from views.manager_view import ManagerView
import os


class ManagerController:

    INSTANCE = None

    def __init__(self, manager: Manager):
        if self.INSTANCE is not None:
            raise ValueError("An instantiation already exists!")
        self.user_container = UserContainer.get_instance()
        self.manager = manager

    def start(self):
        should_exit = False
        while not should_exit:
            try:
                os.system('clear')
                ManagerView.display_manager_menu(self.manager.login, 'Manager')
                user_input = ManagerView.get_user_input('Choose an option: ')
                if user_input == '1':
                    self.promote_user_to_mentor()
                elif user_input == '5':
                    self.display_students()
                elif user_input == '6':
                    should_exit = True
            except Exception as e:
                print(e)

    @classmethod
    def get_instance(cls, manager: Manager):
        """
        Returns the singleton instance of Controller
        :return: None
        """
        if cls.INSTANCE is None:
            cls.INSTANCE = ManagerController(manager)
        return cls.INSTANCE

    def promote_user_to_mentor(self):
        """
        Make selected User a Mentor
        """
        users = self.user_container.get_users_list()
        ManagerView.display_users(users)
        user_login = ManagerView.get_promotion_input()
        try:
            user = self.user_container.get_user_by_login(user_login)
            self.user_container.users.append(Mentor(user.get_login(), user.get_password(),
                                                    user.get_phone_number(), user.get_email(),
                                                    user.get_name()))
            self.user_container.remove_user(user)
            ManagerView.display_user_promoted(user)
        except:
            ManagerView.display_user_not_found()


    def remove_mentor(self):
        """
        Remove mentor from list
        """
        mentors = self.user_container.get_mentors_list()
        ManagerView.display_users(mentors)
        while True:
            user_login = ManagerView.get_user_remove_input()
            try:
                user = self.user_container.get_user_by_login(user_login)
                self.user_container.remove(user)
                ManagerView.display_user_deleted(user)
            except:
                ManagerView.display_user_not_found()

    def display_students(self):
        students = self.user_container.get_students_list()
        ManagerView.display_students(students)
