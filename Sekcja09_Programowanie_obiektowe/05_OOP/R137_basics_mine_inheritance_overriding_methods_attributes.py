# R137. Dziedziczenie oraz nadpisywanie metod i atrybutów 

# OOP w Python – dziedziczenie
# Dziedziczenie pozwala na utworzenie klasy, która przejmuje metody oraz atrybuty od innej klasy.
# Wystarczy dodać w nawiasach okrągłych nazwę klasy bazowej (rodzica), po której ma być dziedziczenie.
# Vehicle jest klasą bazową, a np. BaseCar – klasą pochodną.


class Vehicle_:
    def __init__(self) -> None:
        self.brand = "unknown"
        self.name = "unknown"
        self.topSpeed = 100
        self.numWheels = 4

    def printVehicleInfo(self) -> None:
        print(self.brand, self.name, self.topSpeed)

    def printData(self):
        print("Vehicle info:", self.brand, self.name)

vehicle1 = Vehicle_()
vehicle1.printVehicleInfo()  # unknown unknown 100


# Klasa dziedzicząca – używa odziedziczonych atrybutów i metod bez zmian
class BaseCar(Vehicle_):
    def printCarInfo(self) -> None:
        # BaseCar korzysta z odziedziczonych atrybutów
        print("Car brand:", self.brand)
        print("Car name:", self.name)
        # I wywołuje odziedziczoną metodę z klasy Vehicle
        self.printVehicleInfo()

car1 = BaseCar()
car1.printCarInfo()  # Car brand: unknown
                     # Car name: unknown
                     # unknown unknown 100


# Dziedziczenie – zmiana wartości odziedziczonych atrybutów
class ModifiedCar(Vehicle_):
    def printCarInfo(self) -> None:
        # Można zmodyfikować odziedziczone atrybuty wewnątrz metody
        self.brand = "Ford"
        self.name = "Mustang"
        print("Car brand:", self.brand)
        print("Car name:", self.name)
        # Nadal można korzystać z odziedziczonych metod
        self.printVehicleInfo()

car2 = ModifiedCar()
car2.printCarInfo()  # Car brand: Ford
                     # Car name: Mustang
                     # Ford Mustang 100


# Dziedziczenie – nadpisywanie metod z klasy bazowej
class OverriddenCar(Vehicle_):
    # Nadpisanie metody printData z klasy Vehicle
    def printData(self):
        self.brand = "Ford"
        self.name = "Mustang"
        print("Car brand:", self.brand)
        print("Car name:", self.name)

vehicle1.printData()   # Vehicle info: unknown unknown
car3 = OverriddenCar()
car3.printData()       # Car brand: Ford
                       # Car name: Mustang


print("\nWykład - ćwiczenia\n")

class Vehicle:
    def __init__(self, brand, name) -> None:
        self.brand = brand
        self.name = name
        self.topSpeed = 10
        self.numWheels = 4

    def printVehicleInfo(self):
        print("printVehicleInfo:", self.brand, self.name, self.topSpeed, self.numWheels)

    def printNumWheels(self):
        print("Vehicle.printNumWheels:", self.numWheels)

vehicle1 = Vehicle("Vehicle", "basic")
vehicle1.printVehicleInfo() # printVehicleInfo: Vehicle basic 10 4

class Car(Vehicle):
    def printCarInfo(self):
        self.topSpeed = 230
        print("printCarInfo", self.brand, self.name, self.topSpeed, self.numWheels)

    def printVehicleInfo(self):
        print("Car.printVehicleInfo:", self.brand, self.name, self.topSpeed, self.numWheels)

car1=Car("Ford","Mustang")
car1.printCarInfo() # printCarInfo Ford Mustang 230 4
car1.printVehicleInfo() # printVehicleInfo: Ford Mustang 230 4
car1.printNumWheels() # Vehicle.printNumWheels: 4

class SuperCar(Car):
    def reachSpeed300(self):
        print("Super car reached 300!")
        self.topSpeed = 301

superCar1 = SuperCar("Ford", "GT")
superCar1.reachSpeed300() # Super car reached 300!
superCar1.printVehicleInfo() # Car.printVehicleInfo: Ford GT 301 4
superCar1.printNumWheels() # Vehicle.printNumWheels: 4

"""
class Vehicle:
    def __init__(self, brand, name):
        self.brand = brand
        self.name = name
        self.topSpeed = 10
        self.numWheels = 4

    def printVehicleInfo(self):
        print("printVehicleInfo: ", self.brand, self.name
                , self.topSpeed, self.numWheels)

    def printNumWheels(self):
        print("Vehicle.numWheels:", self.numWheels)


vehicle1 = Vehicle("Vehicle", "basic")
vehicle1.printVehicleInfo()

class Car(Vehicle):
    def printCarInfo(self):
        self.topSpeed = 230
        print("printCarInfo: ", self.brand, self.name, 
                self.topSpeed, self.numWheels)

    def printVehicleInfo(self):
        print("Car.printVehicleInfo: ", self.brand, self.name
                , self.topSpeed, self.numWheels)

car1 = Car("Ford", "Mustang")
car1.printCarInfo()
car1.printVehicleInfo()
car1.printNumWheels()


class SuperCar(Car):
    def reachSpeed300(self):
        self.topSpeed = 301
        print("Super car reached 300!")

superCar1 = SuperCar("Ford", "GT")
superCar1.reachSpeed300()
superCar1.printVehicleInfo()
superCar1.printNumWheels()

"""
