from models.user import User
from models.assignment_container import AssignmentContainer
from models.assignment import Assignment


class Student(User):

    def __init__(self, *args, **kwargs):
        self.assignments = list(AssignmentContainer.get_instance().get_assignments_list())
        self.group = None
        self.attendance = 0
        super().__init__(*args, **kwargs)

    def get_grades(self):
        grades = {}
        for assignment in self.assignments:
            if assignment.grade:
                grades[assignment.title] = str(assignment.grade)
        return grades

    def add_student_assigment(self, deadline, title, description):
        assignment = Assignment(deadline, title, description)
        self.assignments.append(assignment)

    def add_submission(self, assignment_index, submission):
        assignment = self.assignments[assignment_index]
        assignment.submission = submission
