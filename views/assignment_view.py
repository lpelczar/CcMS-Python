from colorful_view import ColorfulView


class AssignmentView:
    @staticmethod
    def new_assignment_input(is_title=True):
        if is_title:
            input_message = ColorfulView.format_string_to_yellow('Name your assignment: ')
        else:
            input_message = ColorfulView.format_string_to_blue('Describe this assignment: ')
        string = input(input_message)
        return string
