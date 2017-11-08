class User:

    def __init__(self, login, password, phone_number=None, email=None, name=None):
        self.name = name
        self.login = login
        self.password = password
        self.phone_number = phone_number
        self.email = email

    def get_login(self):
        return self.login

    def get_password(self):
        return self.password

    def get_phone_number(self):
        return self.phone_number

    def get_email(self):
        return self.email

    def get_name(self):
        return self.name

    def set_login(self, login):
        self.login = login

    def set_password(self, password):
        self.password = password

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def set_email(self, email):
        self.email = email

    def set_name(self, name):
        self.name = name

    def __str__(self):
        return 'Name: {} Phone: {} Email: {}'.format(self.name, self.phone_number, self.email)
