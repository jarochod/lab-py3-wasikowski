import models.employee

class Manager(models.employee.Employee):
    def __init__(self, name) -> None:
        super().__init__(name, position="Manager")

    def info(self):
        return f"Jestem menedżerem i mam na imię {self.name}. Zarządzam zespołem!"


