class MentorView:

    @staticmethod
    def display_students_list(students_list):
        for student in students_list:
            print(students_list.index(student), student.get_name())

    @staticmethod
    def display_add_assignment():
        deadline = input('Type in deadline for assignment dd-mm-yyyy: ')
        title = input('Type in title of the assignment: ')
        description = input('Describe your assignment: ')
        return deadline, title, description

    @staticmethod
    def get_grading_values():
        student_index = int(input("Type in student's index: "))
        assignment_index = int(input("Type in assignment's index: "))
        grade = input("Type in grade: ")
        return student_index, assignment_index, grade

    @staticmethod
    def