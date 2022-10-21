"""
Filename    : UMLException.py
Description : Parent class of all error handlers
"""
class UMLException:
    
    def __init__(self, classCode : int, methodCode : int, statusCode : int):
        self.classCode = classCode
        self.methodCode = methodCode
        self.statusCode = statusCode
        self.code = classCode + methodCode + statusCode

    def __str__(self):
        return f"{self.code}"

    def throwStatus(self, *args):
        pass

    def __success(self, *args):
        pass

    def __error(self, *args):
        pass