from models.user_container import UserContainer
from models.manager import Manager
from models.mentor import Mentor
from views.manager_view import ManagerView


class ManagerController:

    def __init__(self, manager: Manager):
        if self.INSTANCE is not None:
            raise ValueError("An instantiation already exists!")
        self.user_container = UserContainer.get_instance()
        self.manager = manager

    def start(self):
        should_exit = False
        while not should_exit:
            try:
                ManagerView.display_manager_menu()
                user_input = ManagerView.get_user_input('Choose an option ')
                if user_input == '1':
                    self.manager.promote_user_to_mentor()
            except Exception as e:
                print(e)

    @classmethod
    def get_instance(cls):
        """
        Returns the singleton instance of Controller
        :return: None
        """
        if cls.INSTANCE is None:
            cls.INSTANCE = ManagerController()
        return cls.INSTANCE

    def promote_user_to_mentor(self):
        """
        Make selected User a Mentor
        """
        users = self.user_container.get_users_list()
        ManagerView.display_users(users)
        while True:
            user_login = ManagerView.get_promotion_input()
            for person in users:
                if person is self.user_container.get_user_by_login(user_login):
                    self.user_container.users.append(Mentor(person.get_login(), person.get_password(),
                                                            person.get_phone_number(), person.get_email(),
                                                            person.get_name()))
                    self.user_container.remove_user(person)
                    ManagerView.display_user_promoted(person)
                    break
            else:
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
            except:
                ManagerView.display_user_not_found()
