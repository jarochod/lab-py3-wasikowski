# R138. Dziedziczenie a konstruktory
# OOP w Python - dziedziczenie - konstruktory

# W dziedziczeniu:
# - Klasa pochodna może dziedziczyć konstruktor klasy bazowej.
# - Jeśli klasa pochodna nie posiada własnego konstruktora, używany jest ten z klasy bazowej.
# - Jeśli klasa pochodna definiuje swój konstruktor, konstruktor klasy bazowej NIE jest wywoływany automatycznie.
# - W takim przypadku należy go wywołać ręcznie, np. przez `super().__init__()` lub `NazwaKlasy.__init__(self, ...)`.

# ===================================================
# PRZYKŁADY DZIEDZICZENIA I DZIAŁANIA KONSTRUKTORÓW
# ===================================================

print("\n# 1. Klasa pochodna nie ma konstruktora (używa bazowego)")

class Person_1:
    def __init__(self, name) -> None:
        self.name = name
        print("Person_1 constructor:", self.name)

class Employee_1(Person_1):
    # Brak konstruktora — dziedziczy ten z klasy bazowej
    def printInfo(self):
        print("Employee_1 info")

employee_1 = Employee_1("Ola")


print("\n# 2. Klasa pochodna ma swój konstruktor (bazowy NIE jest wywoływany)")

class Person_2:
    def __init__(self, name) -> None:
        self.name = name
        print("Person_2 constructor:", self.name)

class Employee_2(Person_2):
    # Konstruktor nadpisuje bazowy, ale go nie wywołuje!
    def __init__(self, name) -> None:
        self.name = name
        print("Employee_2 constructor:", self.name)

    def printInfo(self):
        print("Employee_2 info")

employee_2 = Employee_2("Ala")


print("\n# 3. Klasa pochodna wywołuje ręcznie konstruktor klasy bazowej")

class Person_3:
    def __init__(self, name) -> None:
        self.name = name
        print("Person_3 constructor:", self.name)

class Employee_3(Person_3):
    def __init__(self, name) -> None:
        # Lepszy styl: super().__init__(name)
        super().__init__(name)
        print("Employee_3 constructor:", self.name)

    def printInfo(self):
        print("Employee_3 info")

employee_3 = Employee_3("Anna")


# ===================================================
# ĆWICZENIA – DZIEDZICZENIE WIELOPOZIOMOWE
# ===================================================

print("\n# 4. Klasa bazowa Person")

class Person:
    def __init__(self, name, surname, city):
        self.name = name
        self.surname = surname
        self.city = city
        print("Person constructor!")

    def printPersonData(self):
        print("Person.printPersonData:", self.name, self.surname, self.city)

person1 = Person("Ola", "Kowalska", "Kraków")
person1.printPersonData()


print("\n# 5. Klasa pochodna Employee (dziedziczy z Person)")

class Employee(Person):
    def __init__(self, name, surname, city, companyName, salary):
        super().__init__(name, surname, city)
        self.companyName = companyName
        self.salary = salary
        print("Employee constructor!")

    def printEmployeeData(self):
        print("Employee.printEmployeeData:", self.name, self.surname,
              self.companyName, self.salary)

employee1 = Employee("Kasia", "Kot", "Warszawa", "Tech Ltd", 10000)
employee1.printPersonData()
employee1.printEmployeeData()


print("\n# 6. Klasa Manager dziedziczy z Employee")

class Manager(Employee):
    def __init__(self, name, surname, city, companyName, salary, department):
        super().__init__(name, surname, city, companyName, salary)
        self.department = department
        self.team = []  # Lista pracowników w zespole
        print("Manager constructor!")

    def hireEmployee(self, employee):
        if isinstance(employee, Employee):
            self.team.append(employee)
            print(f"{employee.name} {employee.surname} hired to {self.department}")
        else:
            print("Only Employee instances can be hired.")

    def printManagerData(self):
        print("Manager.printManagerData:", self.name, self.surname, self.city,
              self.companyName, self.salary, self.department)
        print("Team members:")
        for emp in self.team:
            print(f" - {emp.name} {emp.surname}, {emp.companyName}, salary: {emp.salary}")

manager1 = Manager("Ania", "Nowak", "Warszawa", "Tech2 Ltd", 15000, "IT")

employee2 = Employee("Tomek", "Nowak", "Gdańsk", "Tech2 Ltd", 8000)
manager1.hireEmployee(employee2)
manager1.hireEmployee(employee1)

manager1.printPersonData()
manager1.printEmployeeData()
manager1.printManagerData()

