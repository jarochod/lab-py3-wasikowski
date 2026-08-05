# R129. Definicja klasy na podstawie której powstają obiekty

# Programowanie obiektowe w Pythonie - definicja klasy - podsumowanie

# Definicja klasy wymaga słowa kluczowego class, po nim nazwę klasy z dużej litery oraz dwupropek.
# Następnie w klasie można zapisać zmienne oraz metody, na których obiekt będzie operował.


class Person:
    def __init__(self, name, surname, country) -> None:
        self.surname = surname
        self.name = name
        self.country = country

    def getFullName(self):
        return f"Full name: {self.name} {self.surname}"

    def printData(self):
        print(f"{self.name} {self.surname} {self.country}")

person1 = Person("Ola", "Kowalska", "Polska")
print( person1.getFullName() )
person1.printData()
print( type(person1) )

# Uwaga:
# Definicja klasy to tylko szablon na bazie którego powstają obiekty w pamięci komputera.
# Są to "plany konstrukcyjne" wykorzystywane przez Python do powołania instancji obiektu np:
person2 = Person("Ala", "Test", "UK")
