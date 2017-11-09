import random


class ColorfulView:

    colors_txt = {'green txt': '\x1b[1;32;40m', 'yellow txt': '\x1b[1;33;40m',
                  'red txt': '\x1b[0;31;40m', 'blue txt': '\x1b[4;34;40m',
                  'white txt': '\x1b[1;37;40m'}
    colors_ascii = {'ascii purple': '\x1b[1;35;40m', 'ascii red': '\x1b[0;31;40m',
                    'ascii blue': '\x1b[4;34;40m', 'ascii yellow': '\x1b[1;33;40m'}


    @staticmethod
    def format_string_to_green(example_string=''):
        formated_string = '{}{}{}'.format(ColorfulView.colors_txt['green txt'], example_string, '\x1b[0m')
        return formated_string

    @staticmethod
    def format_string_to_red(example_string=''):
        formated_string = '{}{}{}'.format(ColorfulView.colors_txt['red txt'], example_string, '\x1b[0m')
        return formated_string

    @staticmethod
    def format_string_to_yellow(example_string=''):
        formated_string = '{}{}{}'.format(ColorfulView.colors_txt['yellow txt'], example_string, '\x1b[0m')
        return formated_string

    @staticmethod
    def format_string_to_blue(example_string=''):
        formated_string = '{}{}{}'.format(ColorfulView.colors_txt['blue txt'], example_string, '\x1b[0m')
        return formated_string

    @staticmethod
    def format_string_to_white(example_string=''):
        formated_string = '{}{}{}'.format(ColorfulView.colors_txt['white txt'], example_string, '\x1b[0m')
        return formated_string

    @staticmethod
    def format_ascii(example_string=''):
        formated_string = '{}{}{}'.format(ColorfulView.colors_ascii['ascii purple'], example_string, '\x1b[0m')
        return formated_string
