class User:
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"User: {self.name}"
    
    def info(self):
        return f"Jestem użytkownikiem o imieniu {self.name}"