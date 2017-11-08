class StudentView:

    @staticmethod
    def display_student_grades(grades_list:dict):
        if not grades_list:
            print('You have no added grades !')
        print('Assignments with grades:')
        for key, value in grades_list.items():
            print('Assignment name: {}; Grade: {}'.format(key, value))

    @staticmethod
    def display_submission_result(self):
        print('You succesfully added new submission !')