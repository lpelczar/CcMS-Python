import os, pickle

FILE_NAME = 'assignments.csv'

class AssignmentContainer:

    INSTANCE = None

    def __init__(self):
        if self.INSTANCE is not None:
            raise ValueError("An instantiation already exists!")
        self.assignments = []
        self.load_from_file()

    
    @classmethod
    def get_instance(cls):
        """
        Retruns the singleton instance of AssignmentContainer
        :return: None
        """
        if cls.INSTANCE is None:
            cls.INSTANCE = AssignmentContainer()
        return cls.INSTANCE
    
    def save_to_file(self):
        """
        Method saves groups list to file
        :return: None
        """
        if not os.path.exists(FILE_NAME) or os.stat(FILE_NAME).st_size == 0:
            return  # checks if the data file exists, if not it does not load it
        if self.assignments: return  # checks if the list have been loaded before if so it does not load again
        with open(FILE_NAME, 'rb') as input:
            self.assignments = pickle.load(input)  # load object from file


    def load_from_file(self):
        """
        Method load groups list from file
        :return: None
        """
        if not self.assignments:
            return
        with open(FILE_NAME, 'wb') as output:
            pickle.dump(self.assignments, output, pickle.HIGHEST_PROTOCOL)  # saves assignments to file

    def get_assignments_list(self):
        return self.assignments

    def add_assignment(self, assignment):
        self.assignments.append(assignment)
        self.save_to_file()
