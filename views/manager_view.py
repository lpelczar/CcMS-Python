class ManagerView:

    @staticmethod
    def display_manager_menu():
        print('1. Promote user to Mentor\n' +
              '2. Remove Mentor\n' +
              '3. Edit Mentor data\n' +
              '4. Display list of Mentors\n' +
              '5. Display list of students')

    @staticmethod
    def display_users(self, users):
        for k, v in enumerate(users):
            print(k+1 + '. ' + str(v))

    @staticmethod
    def get_promotion_input(self):
        return input('Enter login of the user which do you want to promote to Mentor: ')

    @staticmethod
    def get_user_remove_input(self):
        return input('Enter login of the user which do you want to remove: ')

    @staticmethod
    def display_user_promoted(self, user):
        print('User: {} has been promoted to Mentor'.format(user.get_login()))

    @staticmethod
    def display_user_not_found(self):
        print('User with that name not found!')
