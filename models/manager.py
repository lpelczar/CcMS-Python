from user import User


class Manager(User):

    def __init__(self, login, password, email, phone_number, group_names):
        super().__init__(login, password, email, phone_number)
        self.groups = group_names

    def promote_user_to_mentor(self, user):
        pass

    def remove_mentor(self, mentor, mentors_list):
        if mentor in mentors_list:
            mentors_list.remove(mentor)

        return mentors_list

    def change_mentor_data(self, mentor):
        pass

    def show_mentors(self):
        pass

    def show_students(self):
        pass

    def __str__(self):
        pass
