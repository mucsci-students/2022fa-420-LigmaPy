"""
Filename    : RelationException.py
Description : 
"""

from model.ErrorHandlers.UMLException import UMLException
import UMLClassExceptions as classException
from view.printColors import colors
from ReturnStatus import codes, methods


class RelationException(UMLException):
    def __init__(self, methodCode : int, statusCode : int):
        super().__init__(500, methodCode, statusCode)

    def __str__(self):
        return f"Relationship Error ({self.code})"
    
    def throwStatus(self, *args):
        """
        
        """
        if self.statusCode == codes.SUCCESS:
            print(self.__success())
        else:
            print(self.__error())

    def __success(self):
        """ PRIVATE
        
        """
        output = f"\n{colors.fg.lightgreen}*** Success:"

        """
            TODO: Success
        """

        output = f"{output}{colors.reset}"
        return output

    def __error(self):
        """ PRIVATE
        
        """
        output = f"\n{colors.fg.lightred}*** Error:"

        """
            TODO: Src or dest classes do not exist
            TODO: Relationship does not exist
            TODO: Relationship already exists
            TODO: src and dest are the same class
        """

        output = f"{output}{colors.reset}"
        return output