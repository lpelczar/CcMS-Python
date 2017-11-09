class ManagerView:

    @staticmethod
    def display_manager_menu(user_login, role):
        greeting_message = 'Logged as {} ({}) \n'.format(user_login, role)
        print(greeting_message +
              '1. Promote user to Mentor\n' +
              '2. Remove Mentor\n' +
              '3. Edit Mentor data\n' +
              '4. Display list of Mentors\n' +
              '5. Display list of Students\n'
              '6. Exit manager')

    @staticmethod
    def get_user_input(prompt: str):
        return input(prompt)

    @staticmethod
    def display_actual_list(users):
        print('')
        if not users:
            print('List is empty!')
        for k, v in enumerate(users):
            print(str(k + 1) + '. ' + 'Login: ' + v.get_login() + ' Name: ' +
                  v.get_name() + ' Role: ' + v.__class__.__name__)
        print('')

    @staticmethod
    def display_users(users):
        print('')
        if not users:
            print('List is empty!')
        for k, v in enumerate(users):
            print(str(k + 1) + '. ' + 'Login: ' + v.get_login() + ' Name: ' +
                  v.get_name() + ' Role: ' + v.__class__.__name__)
        input('\nPress ENTER to continue')

    @staticmethod
    def get_promotion_input():
        return input('Enter login of the user which do you want to promote to Mentor: ')

    @staticmethod
    def get_user_remove_input():
        return input('Enter login of the user which do you want to remove: ')

    @staticmethod
    def get_user_edit_input():
        return input('Enter login of the mentor which do you want to modify: ')

    @staticmethod
    def get_new_value():
        return input('Enter new value: ')

    @staticmethod
    def display_wrong_attribute():
        print('There is no such attribute to change!')
        input('\nPress ENTER to continue')

    @staticmethod
    def display_user_promoted(user):
        print('User: {} has been promoted to Mentor'.format(user.get_login()))
        input('\nPress ENTER to continue')

    @staticmethod
    def display_user_deleted(user):
        print('User: {} has been deleted'.format(user.get_login()))
        input('\nPress ENTER to continue')

    @staticmethod
    def get_value_to_change():
        return input('Enter what do you want to change: login, password, phone number, email, name ')

    @staticmethod
    def display_user_not_found():
        print('User with that name not found!')
        input('\nPress ENTER to continue')
