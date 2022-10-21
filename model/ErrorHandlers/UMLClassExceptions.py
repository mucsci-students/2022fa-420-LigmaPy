"""
Filename    : UMLClassExceptions.py
Description : Handles all return status' and messages for UMLClass.py
"""

from model.ErrorHandlers.UMLException import UMLException
from model.ErrorHandlers.ReturnStatus import codes
from view.printColors import colors

class UMLClassException(UMLException):
    def __init__(self, code : int):
        super().__init__(code)

    def __str__(self):
        return f"Class Error ({self.code}):"

    def throwStatus(self, *args):
        """
        Prints a status message

        :param *args: Used to get the name of the class name or names
        """
        if self.code == codes.ADDED_CLASS or self.code == codes.DELETED_CLASS or self.code == codes.RENAMED_CLASS:
            print(self.__success(args[0], args[1]))
        else:
            print(self.__error(args[0], args[1]))

    def __success(self, className : str, newName : str):
        """ PRIVATE
        Prints the success message

        :param className: The name of the class
        :param newName: The new name for the class when being renamed
        :returns: The output message
        """
        
        output = f"{colors.fg.lightgreen}*** Success:"
        
        if self.code == codes.ADDED_CLASS:
            output = f"{output} Added {className} class"
        elif self.code == codes.DELETED_CLASS:
            output = f"{output} Deleted {className} class"
        elif self.code == codes.RENAMED_CLASS:
            output = f"{output} Renamed class {className} to {newName}"

        output = f"{output}{colors.reset}"

        return output

    def __error(self, className : str, newName : str):
        """ PRIVATE
        Prints the error message

        :param className: The name of the class
        :param newName: The new name for the class when being renamed
        :returns: The output message
        """
        output = f"{colors.fg.lightred}*** Class"

        if self.code == codes.ADD_EXISTING_CLASS:
            output = f"{output} Add Error ({self.code}): {className} class already exists"
        elif self.code == codes.ADD_EMPTY_CLASS:
            output = f"{output} Name Error ({self.code}): Class name cannot be empty"
        elif self.code == codes.DELETE_NOT_EXISTING_CLASS:
            output = f"{output} Delete Error ({self.code}): {className} class does not exist"
        elif self.code == codes.RENAME_CLASS_NOT_EXIST:
            output = f"{output} Rename Error ({self.code}): {className} class does not exist"
        elif self.code == codes.RENAME_NEW_CLASS_EXIST:
            output = f"{output} Rename Error ({self.code}): {newName} class already exists"
        elif self.code == codes.RENAME_CLASS_EMPTY:
            output = f"{output} Rename Error ({self.code}): Class name cannot be empty"

        output = f"{output}{colors.reset}"

        return output
