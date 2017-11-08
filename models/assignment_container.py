class AssignmentContainer:
    def __init__(self):
        self.assignments = []

    @staticmethod
    def save_to_file(filename: str = 'assignments.txt'):
        """
                Method loads users list from file
                :return: None
                """
        if not os.path.exists(FILE_NAME) or os.stat(FILE_NAME).st_size == 0:
            return  # checks if the data file exists, if not it does not load it
        if self.users: return  # checks if the list have been loaded before if so it does not load again
        with open(FILE_NAME, 'rb') as input:
            self.users = pickle.load(input)  # load object from file

    @staticmethod
    def load_from_file(filename: str = 'assignments.txt'):
        if not self.users:
            return
        with open(FILE_NAME, 'wb') as output:
            pickle.dump(self.assignments, output, pickle.HIGHEST_PROTOCOL)  # saves assignments to file

    def get_assignments_list(self):
        return self.assignments

    def add_assignment(self, assignment):
        self.assignments.append(assignment)

    def get_assignment(self, index):
        for assignment in self.assigments:
            if self.assignments.index(assignment) == index:
                return assignment


