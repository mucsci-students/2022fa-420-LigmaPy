from model.ErrorHandlers.UMLException import UMLException


class UMLMethodException(UMLException):
    def __init__(self, code : int):
        super().__init__(300+code)

    def __str__(self):
        return f"{self.code}"

    def throwStatus(self):
        return super().throwStatus()