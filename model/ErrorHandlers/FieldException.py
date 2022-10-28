"""
Filename    : FieldException.py
Description : Handles all return status codes for Fields
"""

from model.ErrorHandlers.UMLException import UMLException
from model.ErrorHandlers.ReturnStatus import codes
from view.printColors import colors

class FieldException(UMLException):
    def __init__(self, code : int):
        super().__init__(code)

    def throwStatus(self, *args):
        """
        Prints a status message

        :param *args: Used to get the name of the class name or names
        """
        if self.code == codes.ADDED_FIELD or self.code == codes.DELETED_FIELD or self.code == codes.RENAMED_FIELD:
            print(self.__success(args[0], args[1], args[2]))
        else:
            print(self.__error(args[0], args[1], args[2]))

    def __success(self, className:str, fieldName:str, newName:str=None):
        """ PRIVATE
        Prints the success message

        :param className: The name of the class
        :param fieldName: Name of the field
        :param newName: The new name for the class when being renamed
        :returns: The output message
        """
        output = f"\n{colors.fg.lightgreen}*** Success:"

        if self.code == codes.ADDED_FIELD:
            output = f"{output} Added {fieldName} to {className} class"
        elif self.code == codes.DELETED_FIELD:
            output = f"{output} Deleted {fieldName} from {className} class"
        elif self.code == codes.RENAMED_FIELD:
            output = f"{output} Renamed {fieldName} to {newName} in {className} class"

        return f"{output}{colors.reset}"

    def __error(self, className:str, fieldName:str, newName:str=None):
        """ PRIVATE
        Prints the error message

        :param className: The name of the class
        :param fieldName: The name of the field
        :param newName: The new name for the Field when being renamed DEFAULT: None
        :returns: The output message
        """
        output = f"\n{colors.fg.lightred}*** Field"

        if self.code == codes.ADD_FIELD_NOT_EXISTING_CLASS:
            output = f"{output} Class Add Error ({self.code}): Class {className} does not exist"
        elif self.code == codes.ADD_EXISTING_FIELD:
            output = f"{output} Add Error ({self.code}): {fieldName} already exists in {className} class"
        elif self.code == codes.DELETE_FIELD_NOT_EXISTING_CLASS:
            output = f"{output} Class Delete Error ({self.code}): Class {className} does not exist"
        elif self.code == codes.DELETE_FIELD_NOT_EXISTING_FIELD:
            output = f"{output} Delete Error ({self.code}): {fieldName} does not exist in {className} class"
        elif self.code == codes.RENAME_FIELD_CLASS_NOT_EXIST:
            output = f"{output} Class Rename Error ({self.code}): Class {className} does not exist"
        elif self.code == codes.RENAME_FIELD_FIELD_NOT_EXIST:
            output = f"{output} Rename Error ({self.code}): {fieldName} does not exist in {className} class"
        elif self.code == codes.RENAME_FIELD_NEW_EXISTS:
            output = f"{output} Rename Error ({self.code}): {newName} already exists in {className} class"

        return f"{output}{colors.reset}"