# R135. Statyczna zmienna wspólna dla wszystkich obiektów

# OOP w Python - statyczna zmienna wspólna dla wszystkich obiektów

# Zmienną statyczną tworzymy wewnątrz klasy, poza konstruktorem i metodą.
# Ciekawą właściwością takiej statycznej zmiennej jest fakt, że jest tylko jedną i jedyną
# dla wszystkich instancji obiektu na bazie danej klasy.
# 
# W przykładzie zmienną statyczną jest numEmployees zdefiniowana na poziome klasy.
# Dostęp do niej uzyskuje się poprzez nazwę klasy i nazwę zmiennej statycznej.

print("Wykład\n")

class Emloyee_:
    # statyczna, wspólna zmienna dla wszystkich obiejktów na bazie klasy employee
    numEmployees = 0

    def __init__(self, name) -> None:
        self.name = name # atrybut obiektu
        print(f"self.name: {self.name}")

        # zwiększenie wartości wspólnej statycznej zmiennej
        Emloyee_.numEmployees += 1
        print(f"Employee_.numEmployees {Emloyee_.numEmployees}")

employee_1 = Emloyee_("Ola") # self.name: Ola
                               # Employee_0.numEmployees 1
employee_2 = Emloyee_("Asia")
employee_3 = Emloyee_("Kasia")

print(f"number of employees: {Emloyee_.numEmployees}") # number of employees: 3

#---------------------------------
print("\nWykład - ćwiczenia\n")

class Employee:
    numEmployees = 0
    employeesList = []

    def __init__(self, name) -> None:
        self.name = name

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
employee1.printAllEmployees()


