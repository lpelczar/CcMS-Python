class Assignment:
    def __init__(self, deadline, title, description, grade=None, submission=None):
        self.deadline = deadline
        self.title = title
        self.description = description
        self.grade = grade
        self.submission = submission

    def __str__(self):
        return 'Title: {}, Description: {}, Deadline: {}, Grade: {}, Submission: {}'.format(self.title, self.description, self.deadline, self.grade, self.submission)

    def __repr__(self):
        return 'Title: {}, Description: {}, Deadline: {}, Grade: {}, Submission: {}'.format(self.title, self.description, self.deadline, self.grade, self.submission)