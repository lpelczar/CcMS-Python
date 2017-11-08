from models.user_container import UserContainer
from models.manager import Manager


class ManagerController:

    def __init__(self, manager: Manager):
        if self.INSTANCE is not None:
            raise ValueError("An instantiation already exists!")
        self.user_container = UserContainer.get_instance()
        self.manager = manager

    @classmethod
    def get_instance(cls):
        """
        Returns the singleton instance of Controller
        :return: None
        """
        if cls.INSTANCE is None:
            cls.INSTANCE = ManagerController()
        return cls.INSTANCE
