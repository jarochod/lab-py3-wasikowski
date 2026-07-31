# R140. Hermetyzacja - enkapsulacja gettery i settery

# OOP w Python - hermetyzacja / enkapsulacja gettery i settery
# Dekorator properties pozwala na wywołanie metody ustawiających i pobierających dane z
# prywatnych zmiennych czyli gettery i settery. 


print("\nWykład\n")

class Vehicle_:
    def __init__(self) -> None:
        self.__gears = 5

    @property # getter, pobiera wartość
    def gears(self):
        if(self.__gears > 0):
            return self.__gears
        else:
            return -1
    
    @gears.setter # setter, ustawia wartość
    def gears(self, gears):
        if(gears>0): self.__gears = gears

    def printGears(self):
        print("Grars: ", self.__gears)

vehicle1 = Vehicle_()
vehicle1.gears = 7
vehicle1.printGears()

vehicle1.gears = -2
vehicle1.printGears()



print("\nćwiczenia\n")

class Vehicle:
    def __init__(self):
        pass

    @property
    def gears(self):
        print("getter:", self.__gears)
        if(self.__gears > 0):
            return self.__gears
        else:
            return -1

    @gears.setter
    def gears(self, newGears):
        print("newGears:", newGears)
        if(newGears > 0): self.__gears = newGears


vehicle1 = Vehicle()
vehicle1.gears = 8
print(vehicle1.gears)
