import hashlib
import os
import time
from controllers.key_getch import getch


class PasswordService:

    @staticmethod
    def encrypt_password(password):
        secure_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
        return secure_hash

    @staticmethod
    def get_password_with_asterisks():
        password = []
        password_created = False
        while not password_created:
            os.system('clear')
            print('*' * (len(password if password else 1) - 1) + password[-1] if password else '')
            print('Enter password: ', end='')
            time.sleep(0.3)
            os.system('clear')
            print('*' * len(password))
            x = getch()
            if x == '\r':
                password_created = True
            password.append(x)
        return ''.join(password)