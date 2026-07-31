# R141. Moduły instrukcja import oraz from import

from user import User

class Employee(User):
    def __init__(self, name) -> None:
        super().__init__(name)

    def __str__(self) -> str:
        return f"Employee: {self.name}"