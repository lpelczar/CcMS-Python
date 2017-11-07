import os


class RootView:

    def clear_screen(self):
        self.os.system('clear')

    def display_starting_screen(self, file_name='welcome_screen.txt'):
        self.clear_screen()
        with open(file_name) as f:
            reader = f.read()
        print(reader)

    def display_main_menu(self):
        welcome_information = '\nWelcome in Canvas, patch 0.-2XYZ.4C version.'
        exit_program = '\n0. Exit'
        menu_options = ['Sing in', 'Sing up']
        number_option = 1

        print(welcome_information)
        for option in menu_options:
            number_option = str(number_option)
            print(number_option, option)
            number_option = int(number_option)
            number_option += 1
        print(exit_program)

    def display_sing_in_menu(self):
        self.clear_screen()
