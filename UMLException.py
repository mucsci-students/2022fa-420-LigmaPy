from view.printColors import colors

class UMLException(Exception):
    def __init__(self, *args):
        if args and len(args) == 1:
            self.type = None
            self.message = args[0]
        elif args and len(args) > 1:
            self.type = args[0]
            self.message = args[1]
        else:
            self.type = None
            self.message = None

    def __str__(self):
        if self.type and self.message:
            return f'\n{colors.fg.lightred}*** {self.type}: {self.message}{colors.reset}'
        elif self.message:
            return f'\n{colors.fg.lightred}*** Error: {self.message}{colors.reset}'
        else:
            return f'\n*** Error: Type \'help\' for help'


class UMLSuccess():
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'\n{colors.fg.lightgreen}*** Success: {self.message}{colors.reset}'
        else:
            return f'\n*** Success'