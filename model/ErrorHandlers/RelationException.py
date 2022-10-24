"""
Filename    : RelationException.py
Description : Handles all return status codes for relationships
"""

from model.ErrorHandlers.UMLException import UMLException
from view.printColors import colors
from model.ErrorHandlers.ReturnStatus import codes


class RelationException(UMLException):
    def __init__(self, code : int):
        super().__init__(code)

    def __str__(self):
        return f"Relationship Error ({self.code})"
    
    def throwStatus(self, *args):
        """
        Prints a status message

        :param *args: Used to get the name of the class name or names
        """
        if self.code == codes.ADDED_RELATIONSHIP or self.code == codes.DELETED_RELATIONSHIP:
            print(self.__success(args[0], args[1]))
        else:
            print(self.__error(args[0], args[1]))

    def __success(self, src:str, dest:str):
        """ PRIVATE
        Prints the success message

        :param src: The name of the relationship's source class
        :param dest: The name of the relationship's destination class
        :returns: The output message
        """
        output = f"\n{colors.fg.lightgreen}*** Success:"

        if self.code == codes.ADDED_RELATIONSHIP:
            output = f"{output} Added relationship {colors.bold}[{src}]-[{dest}]"
        elif self.code == codes.DELETED_RELATIONSHIP:
            output = f"{output} Deleted relationship {colors.bold}[{src}]-[{dest}]"

        output = f"{output}{colors.reset}"
        return output

    def __error(self, src:str, dest:str):
        """ PRIVATE
        Prints the error message

        :param src: The relationship's source class
        :param dest: The relationship's destination class
        :returns: The output message
        """
        output = f"\n{colors.fg.lightred}*** Relationship"

        if self.code == codes.ADD_SRC_NOT_EXIST:
            output = f"{output} Source Class Error ({self.code}): The source class does not exist"
        elif self.code == codes.ADD_DEST_NOT_EXIST:
            output = f"{output} Destination Class Error ({self.code}): The destination class does not exist"
        elif self.code == codes.ADD_INVALID_TYPE:
            pass
        elif self.code == codes.ADD_SAME_SRC_DEST:
            output = f"{output} Error ({self.code}): Source and destination cannot be the same class"
        elif self.code == codes.ADD_EXISTING_RELATIONSHIP:
            output = f"{output} Add Error ({self.code}): Relationship [{src}]-[{dest}] already exists"
        elif self.code == codes.DELETE_NOT_EXISTING_RELATIONSHIP:
            output = f"{output} Delete Error ({self.code}): The relationship [{src}]-[{dest}] does not exist"
        elif self.code == codes.DELETE_NOT_EXISTING_SRC:
            output = f"{output} Delete Source Class Error ({self.code}): {src} class does not exist"
        elif self.code == codes.DELETE_NOT_EXISTING_DEST:
            output = f"{output} Delete Destination Class Error ({self.code}): {dest} class does not exist"

        output = f"{output}{colors.reset}"
        return output