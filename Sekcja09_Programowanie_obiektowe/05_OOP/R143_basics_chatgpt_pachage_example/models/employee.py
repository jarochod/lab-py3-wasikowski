import models.user

class Employee(models.user.User):
    def __init__(self, name, position="Employee") -> None:
        print(f"Employee.__init__ wywołany z name={name}, position={position}")
        super().__init__(name)
        self.position = position

    def __str__(self) -> str:
        return f"{self.position}: {self.name}"
