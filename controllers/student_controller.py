import os, traceback
from models.student import Student
from models.user_container import UserContainer
from views.student_view import StudentView
from models.assignment_container import AssignmentContainer

class StudentController:

    INSTANCE = None

    def __init__(self, student:Student):
        if self.INSTANCE is not None:
            raise ValueError("An instantiation already exists!")
        self.user_container = UserContainer.get_instance()
        self.student = student

    def start(self):
        """
        Main method of StudentController
        :return: None
        """
        should_exit = False
        self.update_user_assignments()
        while not should_exit:
            try:
                os.system('clear')
                StudentView.display_student_menu(self.student.login, 'Student')
                user_input = StudentView.get_user_input('Choose an option: ')
                if user_input == '1':
                    self.submit_assignment()
                    StudentView.display_submission_result()
                elif user_input == '2':
                    self.show_student_grades()
                elif user_input == '3':
                    should_exit = True
            except IndexError:
                StudentView.print_wrong_assignment_id_error()
            except ValueError:
                StudentView.print_wrong_assignment_id_error()
            except Exception:
                tb = traceback.format_exc()
                print(tb)
                input()
        os.system('clear')



    @classmethod
    def get_instance(cls, student:Student):
        """
        Returns the singleton instance of Controller
        :return: None
        """
        if cls.INSTANCE is None:
            cls.INSTANCE = StudentController(student)
        return cls.INSTANCE

    def show_student_grades(self):
        """
        Show grades for student with given student login
        """
        assignments_with_grades = [assignment for assignment in self.student.assignments if
                                         assignment.grade != None]
        if not self.student.assignments:
            StudentView.print_user_have_no_grades()
        assignments_as_strings_list = []
        for assignment in assignments_with_grades:
            grade_with_assignment_name = 'Grade: {}, Assignment title: {}'.format(assignment.grade,assignment.title)
            assignments_as_strings_list.append(grade_with_assignment_name)
        StudentView.display_user_grades(assignments_as_strings_list)


    def submit_assignment(self):
        """
        Add new key to submissions with assignment_name
        """
        assignment_without_submission = [assignment for assignment in self.student.assignments if
                                         assignment.submission == None]
        if not assignment_without_submission:
            StudentView.print_user_assignments_list_empty_error()
            return
        assignments_as_strings_list = [str(assignment) for assignment in assignment_without_submission]
        StudentView.display_user_assignments(assignments_as_strings_list)
        submission_id = int(StudentView.get_user_input('Type submission ID: '))
        submission_content = StudentView.get_user_input('Type link to github repository: ')
        self.student.add_submission(assignment_without_submission[submission_id].title, submission_content)
        UserContainer.get_instance().save_users_to_file()

    def update_user_assignments(self):
        """
        Updates missing assignments after user login.
        :return:
        """
        for global_assignment in AssignmentContainer.get_instance().get_assignments_list():
            add_assignment = True
            for user_assignment in self.student.assignments:
                if user_assignment.title == global_assignment.title:
                    add_assignment = False
                    break
            if add_assignment:
                self.student.add_student_assignment(global_assignment.deadline, global_assignment.title,
                                                    global_assignment.description)


