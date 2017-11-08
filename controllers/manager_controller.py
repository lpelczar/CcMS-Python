from models.user_container import UserContainer
from models.manager import Manager
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
                user_input = ManagerView.get_user_input('Choose an option')
                if user_input == '1':
                    self.manager.
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
        users = self.user_container.get_users_list()
        ManagerView.display_users()
        while True:
            user_login = ManagerView.get_promotion_input()
            for user in users:
                if user_login == user.get_login():
