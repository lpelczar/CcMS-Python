class AssignmentView:
    def new_assignment_input(self, is_title=True):
        if is_title:
            input_message = 'Name your assignment: '
        else:
            input_message = 'Describe this assignment: '
        string = input(input_message)
        return string
