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
        """
        Prints a status message

        :param *args: Used to get the name of the class name or names
        """
        if self.code == codes.ADDED_METHOD or self.code == codes.DELETED_METHOD or self.code == codes.RENAMED_METHOD:
            print(self.__success(args[0], args[1], args[2]))
        else:
            print(self.__error(args[0], args[1], args[2]))

    def __success(self, className : str, methodName : str, newName : str):
        """ PRIVATE
        Prints the success message

        :param className: The name of the class
        :param methodName: The name of the method
        :param newName: The new name for the method when being renamed
        :returns: The output message
        """
        output = f"\n{colors.fg.lightgreen}*** Success:"
        if self.code == codes.ADDED_METHOD:
            output = f"{output} Added method {methodName} to {className} class"
        elif self.code == codes.DELETED_METHOD:
            output = f"{output} Deleted method {methodName} from {className} class"
        elif self.code == codes.RENAMED_METHOD:
            output = f"{output} Renamed method {methodName} to {newName} in {className} class"

        output = f"{output}{colors.reset}"
        return output

    def __error(self, className : str, methodName : str, newName : str):
        """ PRIVATE
        Prints the error message

        :param className: The name of the class
        :param methodName: The name of the method
        :param newName: The new name for the method when being renamed
        :returns: The output message
        """
        output = f"\n{colors.fg.lightred}*** Method"

        if self.code == codes.ADD_NOT_EXISTING_CLASS:
            output = f"{output} Class Error ({self.code}): {className} class does not exist"
        elif self.code == codes.ADD_EXISTING_METHOD:
            output = f"{output} Add Error ({self.code}): Method {methodName} already exists"
        elif self.code == codes.DELETE_METHOD_NOT_EXISTING_CLASS:
            output = f"{output} Class Error ({self.code}): {className} class does not exist"
        elif self.code == codes.DELETE_NOT_EXISTING_METHOD:
            output = f"{output} Delete Error ({self.code}): Method {methodName} does not exist"
        elif self.code == codes.RENAME_METHOD_CLASS_NOT_EXIST:
            output = f"{output} Rename Error ({self.code}): Class {className} does not exist"
        elif self.code == codes.RENAME_METHOD_METHOD_NOT_EXIST:
            output = f"{output} Rename Error ({self.code}): Method {methodName} does not exist"
        elif self.code == codes.RENAME_METHOD_NEW_EXISTS:
            output = f"{output} Rename Error ({self.code}): Method {newName} already exists"

        output = f"{output}{colors.reset}"
        return output