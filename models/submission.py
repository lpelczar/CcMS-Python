from datetime import datetime

class Submission:

    def __init__(self, title:str, description:str, date:datetime):
        """
        Constructor of submission.
        :param title: str -> title of submission
        :param description: str -> description of submission
        :param date: datetime -> date of submission commitment
        """
        self.title = title
        self.description = description
        self.datetime = datetime