# R136. DocString oraz inne przydatne metody i atrybuty w klasie

# OOP w Python - definicja klasy - string dokumentujący

# String dokumentujący to łańcuch znaków w pierwszej linijce definicji funkcji, metody
# czy klasy. Może być pobrany za pomocą nazwy klasy oraz strybutu __doc__
# 
# Takie łańcuchy stanowią opis działania danej funkcjionalności większej części kodu
# np klasy, modułu itd. Nie należy mylić tych informacji z komentarzami, które opisują
# konkretny kod np. jak działa. 

# Jest wiele zmiennych oraz metod pozwalających na dostęp o informacji o klasie/obiekcie
# oraz atrybutach.



print("Wykład\n")

class Person:
    'String do dokumentacji: klasa Person opisująca osobę'
    def __init__(self, name, surname) -> None:
        print( Person.__name__ ) # Person / nazwa klasy
        self.name = name
        self.surname = surname
        self.printDocString()

        # nazwa modułu w którym zdefiniowana jest klasa
        print( Person.__module__) # __main__ w trybie interaktywnym
        # czy istnieje atrybut w obiekcie
        print( hasattr(self, "city")) # False
        print( hasattr(self, "name")) # True
        print( getattr(self, "name")) # Ola / pobranie wartości atrybutu
        self.country = None
        setattr(self, "country", "Poland") # ustawienie nowego atrybutu
        print(self.country)
        print( hasattr(self, "country")) # True
        delattr(self, "country") # skasowanie atrybutu
        print( hasattr(self, "country")) # False


    def printDocString(self):
        print( Person.__doc__)

person1 = Person("Ola", "Kowalska")

#---------------------------------
print("\nWykład - ćwiczenia\n")

class Employee:
    "Employee class describing company employee"
    # static variables for all objects based on Employee
    numEmployees = 0
    employeesList = []

    def __init__(self, name) -> None:
        "Construktor for Employee"
        """
            linia 1
            linia 2
        """
        self.name = name
        self.city: str | None = None

        Employee.numEmployees += 1
        print(self.name, "numEmployees:", Employee.numEmployees)

        Employee.employeesList.append(self)

    def printAllEmployees(self):
        for el in Employee.employeesList:
            print(el.name)

employee1 = Employee("Ola")
employee2 = Employee("Kasia")
employee3 = Employee("Adam")
employee4 = Employee("Karol")

print("EEmployee.numEmployees:", Employee.numEmployees)
print()

employee1.printAllEmployees()

help(Employee)
print("----------")

print(Employee.__doc__) # Employee class describing company employee
print(Employee.__name__) # Employee
print(Employee.__module__) # __main__

print("name attr in Employee", hasattr(employee1, "name")) # name attr in Employee True
print("city attr in Employee", hasattr(employee1, "city")) # city attr in Employee False
employee1.city = "Krk" 
print("city attr in Employee", hasattr(employee1, "city")) # city attr in Employee True

setattr(employee1, "name", "Kasia")
print("employee1.name:", getattr(employee1, "name"))
