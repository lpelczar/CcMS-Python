class Assignment:
def __init__(self, deadline, title, description, grade=None, submission=None ):
        self.deadline = deadline
        self.title = title
        self.description = description
        self.submission = submission
        self.grade = grade