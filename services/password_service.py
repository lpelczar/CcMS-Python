import hashlib
import os
import time
from views.colorful_view import ColorfulView
from controllers.key_getch import getch


class PasswordService:

    @staticmethod
    def encrypt_password(password):
        """
        Hash password using sha256
        :param password: string -> user password
        :return:
        """
        secure_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
        return secure_hash

    @staticmethod
    def get_password_with_asterisks():
        """
        Hide password while typing
        :return:
        """
        password = []
        password_created = False
        while not password_created:
            os.system('clear')
            print('*' * (len(password if password else 1) - 1) + password[-1] if password else '')
            print(ColorfulView.format_string_to_yellow('Enter password') + '(press ESC to back):', end='')
            time.sleep(0.1)
            os.system('clear')
            print('*' * len(password))
            print(ColorfulView.format_string_to_yellow('Enter password') + '(press ESC to back):', end='')
            x = getch()
            if x == chr(27):
                raise RuntimeError("User pressed ESC in password creator")
            elif x == '\r':
                print('')
                password_created = True
            elif x == '\x7f':
                if password:
                    del password[-1]
            else:
                password.append(x)
        return ''.join(password)
