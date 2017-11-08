class MentorView:

    @staticmethod
    def display_students_list(students_list):
        for student in students_list:
            print(student)

    @staticmethod
    def display_add_assignment():
        deadline = input('Type in deadline for assignment: ')
        title = input('Type in title of the assignment: ')
        description = input('Describe your assignment: ')
        return deadline, title, description