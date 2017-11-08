class AssignmentContainer:
    def __init__(self):
        self.assignments = []

    @staticmethod
    def save_to_file(filename: str = 'assignments.txt'):
        pass

    @staticmethod
    def load_from_file(filename: str = 'assignments.txt'):
        pass

    def get_assignments_list(self):
        return self.assignments

    def add_assignment(self, assignment):
        self.assignments.append(assignment)

    def get_assignment(self, index):
        for assignment in self.assigments:
            if self.assignments.index(assignment) == index:
                return assignment
