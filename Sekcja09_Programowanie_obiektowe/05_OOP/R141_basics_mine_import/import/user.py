# R141. Moduły instrukcja import oraz from import

class User:
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"User: {self.name}"

if __name__ == "__main__":
    user1 = User("Ola")
    print(user1)