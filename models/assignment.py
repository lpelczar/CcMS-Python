import view/assignment_view

class Assignment():
    def __init__(self):
        self.assignments = {}

    def add_assignment(self):
        title = assignment_view.new_assignment_input()
        self.assignments[title] = assignment_view.new_assignment_input(False)

    @staticmethod
    def save_to_file(filename:str = 'assignments.txt'):
        dictionary = self.assignments
        with open(filename, 'w') as file:
            for key, value in dictionary.items():
                file.write(str(value) + ';' + str(key) + '\n')

    @staticmethod
    def load_from_file(filename:str = 'assignments.txt'):
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                splitted_line = line.split(';')
                title = splitted_line[0]
                description = splitted_line[1]
                self.assignments[title] = description
