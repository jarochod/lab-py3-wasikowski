# R131. Konstruktor wewnątrz klasy - zadanie

# Wersja rozbudowana o eleganckie formatowanie napisu (funkcja join + spójnik 'i')
# oraz reprezentację tekstową obiektu za pomocą metody specjalnej __str__.

# Zadanie - klasa do tworzenia pizzy
# Stworzysz teraz prostą klasę Pizza, która pozwoli na tworzenie
# obiektu pizzy z listą składników.
#
# 1) Zdefiniuj klasę Pizza z konstruktorem (__init__), który tworzy
#    atrybut `ingredients` (składniki), będący pustą listą na start.
# 2) Dodaj metodę `addIngredient`, która przyjmuje jeden parametr
#    (oprócz self) - składnik (ingredient) do dodania do pizzy.
#    Sprawdź, czy składnik jest typu str, jeśli tak - dodaj go do listy.
# 3) Dodaj metodę `showIngredients`, która wyświetla wszystkie
#    składniki pizzy.
# 4) Stwórz instancję klasy Pizza.
# 5) Dodaj składniki do pizzy używając metody `addIngredient`:
#    "ser", "pomidor", "pieczarki"
# 6) Wyświetl składniki pizzy wywołując metodę `showIngredients`.


class Pizza:
    def __init__(self) -> None:
        # Inicjalizacja pustej listy składników
        self.ingredients = []

    def addIngredient(self, ingredient: str) -> None:
        # Dodanie składnika tylko wtedy, gdy jest ciągiem znaków (str)
        if isinstance(ingredient, str):
            self.ingredients.append(ingredient)
        else:
            print('Dane nieprawidłowe')

    def __str__(self) -> str:
        # Zwraca czytelną reprezentację tekstową składników pizzy
        if not self.ingredients:
            return "brak składników"
        if len(self.ingredients) == 1:
            return self.ingredients[0]
        return ", ".join(self.ingredients[:-1]) + f" i {self.ingredients[-1]}"

    def showIngredients(self) -> None:
        # {self} automatycznie wywołuje powyższą metodę __str__
        print(f"Składniki: {self}")


# Test działania:
pizza = Pizza()
pizza.showIngredients()

pizza.addIngredient("ser")
pizza.showIngredients()

pizza.addIngredient("pomidor")
pizza.showIngredients()

pizza.addIngredient("pieczarki")
pizza.showIngredients()


# --Wynik--
# Składniki: brak składników
# Składniki: ser
# Składniki: ser i pomidor
# Składniki: ser, pomidor i pieczarki






