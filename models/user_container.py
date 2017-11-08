import pickle, os
from models.student import Student
from models.employee import Employee
from models.mentor import Mentor

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
        Retruns the singleton instance of Controller
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
        Getter of users.
        :return:
        """
        return self.users

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

    def add_user(self, user):
        """
        Methods add user to users and save to file.
        :param user: User -> user object
        :return: None
        """
        if self.get_user(user.login, user.password) == None :
            self.users.append(user)
            self.save_users_to_file()

    def remove_user(self, user):
        """
        Methods remove user from users and save updated users list to file.
        :param user: User -> user object
        :return: None
        """
        self.users.remove(user)
        self.save_users_to_file()
