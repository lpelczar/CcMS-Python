import os, pickle
from models.user_container import UserContainer
from models.student import Student

GROUPS_FILE_PATH = 'groups.csv'

class Group():

    groups_list: []

    def __init__(self, name:str):
        Group.load_groups_from_file()
        if name in Group.groups_list: raise AttributeError('Such group already exists !')
        self.name = name
        Group.groups_list.append(self)
        Group.save_groups_to_file()


    @staticmethod
    def save_groups_to_file():
        """
        Method saves todo_items_list list to file as binary object
        :return: None
        """
        with open('todoitems.data', 'wb') as output:
            pickle.dump(Group.groups_list, output, pickle.HIGHEST_PROTOCOL) #saves object to file

    @staticmethod
    def load_groups_from_file():
        """
        Method loads groups list from file
        :return: None
        """
        if not os.path.exists(GROUPS_FILE_PATH) or os.stat(GROUPS_FILE_PATH).st_size == 0:
            return  # checks if the data file exists, if not it does not load it
        if Group.groups_list: return #checks if the list have been loaded before if so it does not load again
        with open('todoitems.data', 'rb') as input:
            Group.groups_list = pickle.load(input) #load object from file

    @staticmethod
    def get_students_by_group(group_name:str):

        #gets all students from UserContainer's users list using list comprehension
        students_list = [user for user in UserContainer.get_instance().get_users_list() if isinstance(user, Student)]

        students_by_group_list = [student for student in students_list if student.group.lower() == group_name.lower()]

        return students_by_group_list

    @staticmethod
    def add_student_to_group(group_name:str, student:Student):
        if group_name not in Group.groups_list: raise AttributeError('Such group does not exist !')
        student.group = group_name

    @staticmethod
    def remove_student_from_group(student:Student):
        student.group == None

    @staticmethod
    def get_groups():
        Group.load_groups_from_file()
        return Group.groups_list




