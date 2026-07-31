# R130. Konstruktor klasy

# W klasie może być zdefiniowana specjalna metoda, tzw. konstruktor, o nazwie __init__, 
# który będzie wywołany podczas tworzenia instancji obiektu, np.: person2 = Person("Ala", "Test", "UK").
# Konstruktor zwykle służy do inicjalizacji zmiennych wewnątrz klasy wartościami przekazanymi jako argumenty, 
# a także do wykonania innych potrzebnych operacji.
# 
# Uwaga: Każda metoda w klasie, w tym konstruktor, zawsze przyjmuje obowiązkowy pierwszy argument self,
# który wskazuje na aktualny obiekt, na którym operujemy podczas wywołania metody/konstruktora.
# Dzięki self możemy zmieniać wartości zmiennych w obiekcie oraz wywoływać inne metody.

class Person:
    def __init__(self, name, surname, country) -> None:
        self.name = name
        self.surname = surname
        self.country = country
    
    def getFullName(self):
        return self.name + " " + self.surname
    
    def printData(self):
        print(f"{self.name} {self.surname} {self.country}")

person1 = Person("Ola", "Kowalska", "Polska")
print("Pełne imię i nazwisko:", person1.getFullName())
person1.printData()


print("\nwyklad - ćwiczenia")
# wersja poprawiona, bo były problemy z int / str
class Book:
    def __init__(self, author, title="unknown", isbn="unknown", year: int | str = "unknown") -> None:
        self.author = author
        self.title = title
        self.isbn = isbn
        self.year = str(year)  # Zamiana na string, aby uniknąć problemów z typami
    
    def printData(self):
        print(self.author, self.title, self.isbn, self.year)

# Przykłady użycia:
book1 = Book("Ola Kowalska", "Podróże", "12345XC", 2020)
book1.printData()  # Ola Kowalska Podróże 12345XC 2020

# Argumenty opcjonalne – nie trzeba podawać wszystkich danych
book2 = Book("Adam", year=2010)
book2.printData()  # Adam unknown unknown 2010


"""
# Wersja z kursu

class Book:
    def __init__(self, author, title ="unknown", isbn = "unknown", year = "unknown"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year

    def printData(self):
        print(self.author, self.title, self.isbn, self.year)


book1 = Book("Ola Kowalska", "Podróże", "122345XC", 2020)
book1.printData()

book2 = Book("Adam", year = 2010)
book2.printData()
"""