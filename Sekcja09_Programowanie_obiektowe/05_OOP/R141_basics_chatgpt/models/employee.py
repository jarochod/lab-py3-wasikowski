import models.user

class Employee(models.user.User):
    def __init__(self, name, position="Employee") -> None:
        super().__init__(name)
        self.position = position

    def __str__(self) -> str:
        return f"{self.position}: {self.name}"
    
    def info(self):
        return f"Jestem pracownikiem na stanowisku {self.position}, nazywam się {self.name}"
