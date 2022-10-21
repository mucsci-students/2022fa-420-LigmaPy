"""
Filename    : UMLClassExceptions.py
Description : Handles all return status' and messages for UMLClass.py
"""
# Fields : 200
# Methods : 300
# Parameters : 400
# Relationships : 500

from model.ErrorHandlers.UMLException import UMLException
from model.ErrorHandlers.ReturnStatus import codes, methods
from view.printColors import colors

class UMLClassException(UMLException):
    def __init__(self, methodCode : int, statusCode : int):
        super().__init__(100, methodCode, statusCode)

    def __str__(self):
        return f"Class Error ({self.code}):"

    def throwStatus(self, *args):
        """
        Prints a status message

        :param *args: Used to get the name of the class name or names
        """
        if self.statusCode == 1:
            print(self.__success(args))
        else:
            print(self.__error(args))

    def __success(self, *args):
        """ PRIVATE
        Prints the success message

        :param *args: Used to get the name of the class name or names
        :returns: The output message
        """
        
        output = f"{colors.fg.lightgreen}*** Success: "
        if self.methodCode == methods.ADD:
            output = f"{output}Added {args[0][0]}"
        elif self.methodCode == methods.DELETE:
            output = f"{output}Deleted {args[0][0]}"
        elif self.methodCode == methods.RENAME:
            output = f"{output}Renamed {args[0][0]} to {args[0][1]}"

        output = f"{output}{colors.reset}"

        return output

    def __error(self, *args):
        """ PRIVATE
        Prints the error message

        :param *args: Used to get the name of the class name or names
        :returns: The output message
        """
        output = f"{colors.fg.lightred}*** Class Name Error "

        if self.statusCode == codes.EMPTY_NAME:
            output = f"{output}({self.code}): Class name cannot be empty"
        elif self.statusCode == codes.EXISTS:
            output = f"{output}({self.code}): Class {args[0][0]} already exists"
        elif self.statusCode == codes.NOT_EXISTS:
            if self.methodCode == methods.RENAME:
                output = f"{output}({self.code}): Class {args[0][1]} does not exist"
            else:
                output = f"{output}({self.code}): Class {args[0][0]} does not exist"

        output = f"{output}{colors.reset}"

        return output
