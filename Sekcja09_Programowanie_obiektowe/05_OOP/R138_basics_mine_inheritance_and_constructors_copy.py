# 📘 Dziedziczenie a konstruktory w Pythonie

# Wprowadzenie:
# - W dziedziczeniu klasa pochodna może dziedziczyć konstruktor klasy bazowej.
# - Jeśli klasa pochodna nie definiuje swojego konstruktora, automatycznie zostanie użyty konstruktor klasy bazowej.
# - Gdy klasa pochodna definiuje własny konstruktor, należy ręcznie wywołać konstruktor klasy bazowej, jeśli chcemy go użyć.

# 🔹 Przykład 1: Tylko klasa bazowa ma konstruktor
class Person_1:
    def __init__(self, name) -> None:
        self.name = name
        print("Person_1 constructor", self.name)

class Employee_1(Person_1):
    def printInfo(self):
        print("Employee_1 info")

# Klasa `Employee_1` nie ma konstruktora, więc używa konstruktora klasy `Person_1`.
employee_1 = Employee_1("Ola")  # -> Person_1 constructor Ola

print()

# 🔹 Przykład 2: Obie klasy mają własne konstruktory
class Person_2:
    def __init__(self, name) -> None:
        self.name = name
        print("Person_2 constructor", self.name)

class Employee_2(Person_2):
    def __init__(self, name) -> None:
        self.name = name
        print("Employee_2 constructor", self.name)

    def printInfo(self):
        print("Employee_2 info")

# Konstruktor klasy bazowej nie jest wywoływany automatycznie, ponieważ został nadpisany.
employee_2 = Employee_2("Ala")  # -> Employee_2 constructor Ala

print()

# 🔹 Przykład 3: Wywołanie konstruktora klasy bazowej w klasie pochodnej
class Person_3:
    def __init__(self, name) -> None:
        self.name = name
        print("Person_3 constructor", self.name)

class Employee_3(Person_3):
    def __init__(self, name) -> None:
        Person_3.__init__(self, name)  # Wywołanie konstruktora nadrzędnego
        print("Employee_3 constructor", self.name)

    def printInfo(self):
        print("Employee_3 info")

employee_3 = Employee_3("Anna")

print()

# ✅ Dobrą praktyką jest używanie `super()` zamiast bezpośredniego wywoływania `NazwaKlasy.__init__`.

# 🧪 Ćwiczenia – Dziedziczenie wielopoziomowe z konstruktorami

# 🧩 Klasa bazowa `Person`
class Person:
    def __init__(self, name, surname, city):
        self.name = name
        self.surname = surname
        self.city = city
        print("Person constructor!")

    def printPersonData(self):
        print("Person.printPersonData:", self.name, self.surname, self.city)

person1 = Person("Ola", "Kowalska", "Krk")
person1.printPersonData()

print()

# 🧩 Klasa pochodna `Employee`
class Employee(Person):
    def __init__(self, name, surname, city, companyName, salary):
        Person.__init__(self, name, surname, city)  # Wywołanie konstruktora klasy bazowej
        self.companyName = companyName
        self.salary = salary
        print("Employee constructor!")

    def printEmployeeData(self):
        print("Employee.printEmployeeData:", self.name, self.surname, self.companyName, self.salary)

employee1 = Employee("Kasia", "Kot", "Waw", "Tech Ltd", 10000)
employee1.printPersonData()
employee1.printEmployeeData()

print()

# 🧩 Klasa `Manager` dziedzicząca z `Employee`
class Manager(Employee):
    def __init__(self, name, surname, city, companyName, salary, department):
        Employee.__init__(self, name, surname, city, companyName, salary)  # Wywołanie konstruktora klasy `Employee`
        self.department = department
        print("Manager constructor!")

    def hireEmployee(self):
        print("Hire employee")

    def printManagerData(self):
        print("Manager data:", self.name, self.surname, self.department)

manager1 = Manager("Ania", "X", "Waw", "Tech2 Ltd", 15000, "IT")
manager1.printPersonData()
manager1.printEmployeeData()
manager1.printManagerData()
manager1.hireEmployee()

print()

# 🧠 Podsumowanie

# | Sytuacja | Czy konstruktor klasy bazowej jest wywołany? |
# |----------|----------------------------------------------|
# | Klasa pochodna nie ma konstruktora | ✅ Tak |
# | Klasa pochodna ma własny konstruktor | ❌ Nie (trzeba wywołać ręcznie) |
# | Ręczne wywołanie w klasie pochodnej | ✅ Tak, np. `super().__init__()` lub `BazowaKlasa.__init__(self, ...)` |
