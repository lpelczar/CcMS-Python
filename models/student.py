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
        """Returns users grades list based on submissions"""
        grades = {}
        for assignment in self.assignments:
            if assignment.grade:
                grades[assignment.title] = str(assignment.grade)
        return grades

    def add_student_assignment(self, deadline, title, description):
        """Add new assignment to student"""
        if self.assignments:
            for existing_assignment in self.assignments:
                if existing_assignment.title.lower() == title.lower():
                    return
        assignment = Assignment(deadline, title, description)
        self.assignments.append(assignment)

    def add_submission(self, assignment_title, submission):
        """
        Add new submission for user's assignment
        :param assignment_title: str -> the title of assignment
        :param submission: str -> the submission content
        :return:
        """
        for assignment in self.assignments:
            if assignment.title.lower() == assignment_title:
                assignment.submission = submission


