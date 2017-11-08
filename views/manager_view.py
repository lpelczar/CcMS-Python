class ManagerView:

    @staticmethod
    def display_users(self, users):
        for k, v in enumerate(users):
            print(k+1 + '. ' + str(v))

    @staticmethod
    def get_promotion_input(self):
        return input('Enter login of the user which do you want to promote to Mentor: ')
