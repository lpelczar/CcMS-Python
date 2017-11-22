from views.recovery_view import RecoveryView
from views.root_view import RootView
from services.recovery_service import RecoveryService
import os

class RecoveryController:

    def __init__(self):
        ...


    def start(self):
        """
        Method starts RecoveryController loop
        :return: None
        """
        should_exit = False
        while not should_exit:
            os.system('clear')
            RecoveryView.display_main_menu()
            user_input = RecoveryView.get_user_input('Choose an option: ')

            if user_input == '1':
                self.new_recovery_password_process()
                should_exit = True

            elif user_input == '2':
                should_exit = True

    def new_recovery_password_process(self):
        is_process_finished = False
        while not is_process_finished:
            os.system('clear')
            try:
                user_input_login_or_email = RecoveryView.get_user_input('Type your login or e-mail(or type back): ')
                if user_input_login_or_email == 'back':
                    is_process_finished = True

                else:
                    rs = RecoveryService(user_input_login_or_email)
                    RecoveryView.display_that_token_have_been_sent()

                    user_input_token = RecoveryView.get_user_input('Type your token: ')
                    rs.raise_exception_if_user_token_is_not_correct(user_input_token)

                    os.system('clear')
                    new_password = RootView.create_user_password()
                    rs.change_password(new_password, user_input_token)

                    is_process_finished = True
                    RecoveryView.display_password_changed_successfully()

            except ValueError as e:
                RecoveryView.display_error_message(str(e))
            except AttributeError as e:
                RecoveryView.display_error_message(str(e))
