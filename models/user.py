class User:

    MAX_PASS_LENGTH = 8
    MAX_LOGIN_LENGTH = 10

    def __init__(self, login, password, phone_number, email, name):
        self.name = name
        if login is not None and len(login) > User.MAX_LOGIN_LENGTH:
            self.login = login
        else:
            raise ValueError('Wrong login!')
        if password is not None and len(password) > User.MAX_PASS_LENGTH:
            self.password = password
        else:
            raise ValueError('Wrong password!')
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return 'Name: {} Phone: {} Email: {}'.format(self.name, self.phone_number, self.email)
