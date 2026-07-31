# R134. Destruktor klasy

# Programowanie obiektowe w Python – definicja klasy – destruktor

# Destruktor to specjalna metoda wywoływana, gdy obiekt jest niszczony za pomocą operatora del.
# Zanim obiekt zostanie usunięty z pamięci, destruktor daje nam szansę na wykonanie 
# ostatnich operacji, np. zamknięcie plików itp.

print("\nWykład + przykład")

class Person:
    def __init__(self, name, surname) -> None:
        self.name = name
        self.surname = surname
        print(f"Object created: {self.get_full_name()}")

    def get_full_name(self) -> str:
        return f"{self.name} {self.surname}"
    
    def __del__(self):
        print(f"Zniszczenie obiektu: {self.get_full_name()}")

person1 = Person("Ola", "Kowalska")  # Object created: Ola Kowalska
print(person1.name)  # Ola
print(person1.surname)  # Kowalska
print(f"Full name: {person1.get_full_name()}")  # Full name: Ola Kowalska
del person1  # Zniszczenie obiektu: Ola Kowalska


print("\nWykład - ćwiczenie")

class Dog:
    def __init__(self):
        print("Konstruktor!")

    def __del__(self):
        print("Destruktor!")

dog1 = Dog()
