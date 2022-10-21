"""
Filename    : UMLException.py
Description : Parent class of all error handlers
"""
class UMLException:
    
    def __init__(self, code : int):
        self.code = code

    def __str__(self):
        return f"{self.code}"

    def throwStatus(self, *args):
        pass

    def __success(self, *args):
        pass

    def __error(self, *args):
        pass