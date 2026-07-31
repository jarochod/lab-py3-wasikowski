# R141. Moduły instrukcja import oraz from import
# Moduły - instrukcja from... import

# Instrukcja from import pozwala na import specyficznych elementów do aktualnej przestrzeni nazw 
# naszego programu. Przestrzeń nazw (tzw. namespaces) to w praktyce słownik z unikalnymi nazwami 
# zmiennych jako klucze, a wartości słownika to wartości zmiennych. 

class User:
    def __init__(self, name, suername) -> None:
        self.name = name
        self.suername = suername

    def __str__(self) -> str:
        return f"{self.name} {self.suername}"



class Empolyee(User):
    def __init__(self, name, suername) -> None:
        super().__init__(name, suername)