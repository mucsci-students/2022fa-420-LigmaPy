"""
Filename    : ParamException.py
Description : Handles all return status codes for Parameters
"""

from model.ErrorHandlers.UMLException import UMLException
from model.ErrorHandlers.ReturnStatus import codes
from view.printColors import colors

class ParamException(UMLException):
    def __init__(self, code : int):
        super().__init__(code)

    def throwStatus(self, *args):
        """
        Prints a status message

        :param *args: Used to get the name of the class name or names
        """
        if self.code == codes.ADDED_PARAM or self.code == codes.DELETED_PARAM or self.code == codes.CHANGED_PARAM:
            print(self.__success(args[0], args[1], args[2], args[3]))
        else:
            print(self.__error(args[0], args[1], args[2], args[3]))

    def __success(self, className:str, methodName:str, params:str, newParams:str=None):
        """ PRIVATE
        Prints the success message

        :param className: The name of the class
        :param methodName: Name of the classes method
        :param params: Name of the parameter being manipulated
        :param newParams: The new name for the class when being renamed
        :returns: The output message
        """

        output = f"\n{colors.fg.lightgreen}*** Success:"

        """ TODO """
        if self.code == codes.ADDED_PARAM:
            output = f"{output} Added {params} to {methodName}"
        elif self.code == codes.DELETED_PARAM:
            output = f"{output} Deleted {params} from {methodName}"
        elif self.code == codes.CHANGED_PARAM:
            output = f"{output} Changed {params} to {newParams} in {methodName}"

        return f"{output}{colors.reset}"

    def __error(self, className:str, methodName:str, param:str, newParam:str=None):
        """ PRIVATE
        Prints the error message

        :param className: The name of the class
        :param methodName: The new name for the class when being renamed
        :param param: The name of the parameter being manipulated
        :param newParam: The updated name of the parameter DEFAULT: None
        :returns: The output message
        """
        output = f"\n{colors.fg.lightred}*** Parameter"

        """ TODO """
        if self.code == codes.ADD_PARAM_CLASS_NOT_EXIST:
            output = f"{output} Class Add Error ({self.code}): {className} class does not exist"
        elif self.code == codes.ADD_PARAM_METHOD_NOT_EXIST:
            output = f"{output} Method Add Error ({self.code}): {methodName} method does not exist"
        elif self.code == codes.ADD_PARAM_ALREADY_EXISTS:
            output = f"{output} Add Error ({self.code}): {param} already exists in {methodName}"
        elif self.code == codes.DELETE_PARAM_CLASS_NOT_EXIST:
            output = f"{output} Class Delete Error ({self.code}): {className} class does not exist"
        elif self.code == codes.DELETE_PARAM_METHOD_NOT_EXIST:
            output = f"{output} Method Delete Error ({self.code}): {methodName} does not exist in {className} class"
        elif self.code == codes.DELETE_PARAM_NOT_EXIST:
            output = f"{output} Delete Error ({self.code}): {param} does not exist in {methodName}"
        elif self.code == codes.CHANGE_PARAM_CLASS_NOT_EXIST:
            output = f"{output} Class Change Error ({self.code}): {className} class does not exist"
        elif self.code == codes.CHANGE_PARAM_METHOD_NOT_EXIST:
            output = f"{output} Method Change Error ({self.code}): {methodName} does not exist in {className} class"
        elif self.code == codes.CHANGE_PARAM_ALREADY_EXISTS:
            output = f"{output} Change Error ({self.code}): {newParam} already exists in {methodName}"

        return f"{output}{colors.reset}"