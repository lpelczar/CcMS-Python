from models.user import User


class Mentor(User):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)