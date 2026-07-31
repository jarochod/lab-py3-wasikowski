class User:
    def __init__(self, name) -> None:
        print(f"User.__init__ wywołany z name={name}")
        self.name = name

    def __str__(self) -> str:
        return f"User: {self.name}"
