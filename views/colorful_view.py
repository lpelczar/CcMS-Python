class ColorfulView:

    colors_dict = {'green txt': '\x1b[0;32;40m', 'yellow txt': '\x1b[0;33;40m',
                   'red txt': '\x1b[0;31;40m', 'blue txt': '\x1b[0;34;40m'}

    @staticmethod
    def format_string_to_green(example_string):
        formated_string = '{}{}'.format(ColorfulView.colors_dict['green txt'], example_string)
        return formated_string

    @staticmethod
    def format_string_to_red(example_string):
        formated_string = '{}{}'.format(ColorfulView.colors_dict['red txt'], example_string)
        return formated_string

    @staticmethod
    def format_string_to_yellow(example_string):
        formated_string = '{}{}'.format(ColorfulView.colors_dict['yellow txt'], example_string)
        return formated_string
