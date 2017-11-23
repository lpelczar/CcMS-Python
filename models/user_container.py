import os
import pickle

from models.employee import Employee
from models.mentor import Mentor
from models.student import Student

FILE_NAME = 'users.csv'


class UserContainer():

    INSTANCE = None

    def __init__(self):
        if self.INSTANCE is not None:
            raise ValueError("An instantiation already exists!")
        self.users = []
        self.load_users_from_file()

    @classmethod
    def get_instance(cls):
        """
        Returns the singleton instance of Controller
        :return: None
        """
        if cls.INSTANCE is None:
            cls.INSTANCE = UserContainer()
        return cls.INSTANCE

    def save_users_to_file(self):
        """
        Method saves users list to file.
        :return: None
        """
        if not self.users: return
        with open(FILE_NAME, 'wb') as output:
            pickle.dump(self.users, output, pickle.HIGHEST_PROTOCOL) #saves object to file

    def load_users_from_file(self):
        """
        Method loads users list from file
        :return: None
        """
        if not os.path.exists(FILE_NAME) or os.stat(FILE_NAME).st_size == 0:
            return  # checks if the data file exists, if not it does not load it
        if self.users: return # checks if the list have been loaded before if so it does not load again
        with open(FILE_NAME, 'rb') as input:
            self.users = pickle.load(input) # load object from file

    def get_users_list(self):
        """
        Getter of all users.
        :return:
        """
        return self.users

    def get_users_with_user_range(self):
        """
        Getter of User class objects.
        :return:
        """
        return [user for user in self.get_users_list() if user.__class__.__name__ == 'User']

    def get_students_list(self):
        """
        Extract students instances from user lsit
        :return:
        """
        return [user for user in self.get_users_list() if isinstance(user, Student)]

    def get_employee_list(self):
        """
        Extract employee instances from user lsit
        :return:
        """
        return [user for user in self.get_users_list() if isinstance(user, Employee)]

    def get_mentor_list(self):
        """
        Extract employee instances from user lsit
        :return:
        """
        return [user for user in self.get_users_list() if isinstance(user, Mentor)]

    def get_not_assigned_users_list(self):
        """
        Extract not assigned instances from user list
        :return:
        """
        not_assigned_users = [user for user in self.get_users_list() if not isinstance(user, Mentor)]
        not_assigned_users = [user for user in not_assigned_users if not isinstance(user, Employee)]
        not_assigned_users = [user for user in not_assigned_users if not isinstance(user, Student)]
        return not_assigned_users


    def get_user(self, login:str, password:str):
        """
        Methodd returns User if such objects exists, otherwise it returns None.
        :param login: login attribute of user
        :param password: password attribute of user
        :return: None
        """
        for user in self.users:
            if user.login == login and user.password == password:
                return user
        return None

    def get_user_by_login_or_email(self, login_or_email):
        """
        Returns user instances by login or email
        :param login_or_email: str -> login or email of user instance to be returned
        :return: User -> an instance of user
        """
        for user in self.users:
            if user.login == login_or_email or user.email == login_or_email:
                return user
        return None


    def add_user(self, user):
        """
        Methods add user to users and save to file.
        :param user: User -> user object
        :return: None
        """
        if self.get_user(user.login, user.password) is None:
            self.users.append(user)
            self.save_users_to_file()
        else:
            raise AttributeError('User with this login already exists')

    def remove_user(self, user):
        """
        Methods remove user from users and save updated users list to file.
        :param user: User -> user object
        :return: None
        """
        self.users.remove(user)
        self.save_users_to_file()
