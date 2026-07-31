# R141. Moduły instrukcja import oraz from import

from employee import Employee

class Manager(Employee):
    def __init__(self, name) -> None:
        super().__init__(name)

    def __str__(self) -> str:
        return f"Manager: {self.name}"