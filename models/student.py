from models.user import User
from models.assignment_container import AssignmentContainer
from models.assignment import Assignment


class Student(User):

    def __init__(self, *args, **kwargs):
        self.assignments = assignment_cotainer
        self.submissions_grades = {}  # Dictionary with key: Assignment name, value: grade
        self.group = None
        self.attendance = 0
        super(Student, self).__init__(*args, **kwargs)

    def get_grades(self):
        grades = {}
        for assignment in self.assignments:
            if assignment.grade:
                grades[assignment.title] = str(grade)
        return grades

    def add_student_assigment(self, title, description, date):
        assignment = Assignment(title, description, date)
        self.assignments.add_assignment(assignment)

    def add_submission(self, assignment_index, submission):
        assignment = self.assignments.get_assignment(assignment_index)
        assignment.submission = submission
