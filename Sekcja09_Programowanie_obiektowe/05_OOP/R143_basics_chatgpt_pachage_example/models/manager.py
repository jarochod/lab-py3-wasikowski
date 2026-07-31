import models.employee

class Manager(models.employee.Employee):
    def __init__(self, name) -> None:
        print(f"Manager.__init__ wywołany z name={name}")
        super().__init__(name, position="Manager")
