class ColorfulView:

    colors_dict = {'green txt': '\x1b[3;32;40m', 'yellow txt': '\x1b[0;33;40m',
                   'red txt': '\x1b[0;31;40m', 'blue txt': '\x1b[4;34;40m',
                   'ascii': '\x1b[1;35;40m'}

    @staticmethod
    def format_string_to_green(example_string=''):
        formated_string = '{}{}{}'.format(ColorfulView.colors_dict['green txt'], example_string, '\x1b[0m')
        return formated_string

    @staticmethod
    def format_string_to_red(example_string=''):
        formated_string = '{}{}{}'.format(ColorfulView.colors_dict['red txt'], example_string, '\x1b[0m')
        return formated_string

    @staticmethod
    def format_string_to_yellow(example_string=''):
        formated_string = '{}{}{}'.format(ColorfulView.colors_dict['yellow txt'], example_string, '\x1b[0m')
        return formated_string

    @staticmethod
    def format_string_to_blue(example_string=''):
        formated_string = '{}{}{}'.format(ColorfulView.colors_dict['blue txt'], example_string, '\x1b[0m')
        return formated_string

    @staticmethod
    def format_ascii(example_string=''):
        formated_string = '{}{}{}'.format(ColorfulView.colors_dict['ascii'], example_string, '\x1b[0m')
        return formated_string
