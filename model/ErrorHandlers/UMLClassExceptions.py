# Class : 100
# Fields : 200
# Methods : 300
# Parameters : 400
# Relationships : 500

# Success : 1
# Does not Exist : 2
# Already Exists : 3
# Empty Name : 4
# Invalid Type : 5

class UMLClassException(Exception):
    def __init__(self, errorCode):
        self.code = errorCode