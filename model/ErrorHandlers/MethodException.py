"""
Filename    : MethodException.py
Description : Exception handler for method commands
"""

from model.ErrorHandlers.UMLException import UMLException
from model.ErrorHandlers.ReturnStatus import codes
from view.printColors import colors

class MethodException(UMLException):
    def __init__(self, code : int):
        super().__init__(code)

    def __str__(self):
        return f"Method Error ({self.code})"

    def throwStatus(self, *args):
        if self.code == codes.ADDED_METHOD or self.code == codes.DELETED_METHOD or self.code == codes.RENAMED_METHOD:
            print(self.__success(args[0], args[1], args[2]))
        else:
            print(self.__error(args[0], args[1], args[2]))

    def __success(self, className : str, methodName : str, newName : str):
        """ PRIVATE
        
        """
        output = f"\n{colors.fg.lightgreen}*** Success:"
        if self.code == codes.ADDED_METHOD:
            pass
        elif self.code == codes.DELETED_METHOD:
            pass
        elif self.code == codes.RENAMED_METHOD:
            pass

        output = f"{output}{colors.reset}"
        return output

    def __error(self, className : str, methodName : str, newName : str):
        """ PRIVATE
        
        """
        output = f"\n{colors.fg.lightred}*** Method"

        """
            TODO
        """

        output = f"{output}{colors.reset}"
        return output