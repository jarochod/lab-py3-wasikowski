# R139. Hermetyzacja (enkapsulacja) w Pythonie – OOP

# 🔐 Hermetyzacja to ukrywanie szczegółów działania klasy (np. zmiennych i metod)

# Podkreślenia a dostępność:
# - __nazwa → prywatne (name mangling: _ClassName__nazwa)
# - _nazwa → chronione (umowna konwencja)


# 📌 PRZYKŁAD 1 – Prywatne pola i metody (__)

class Vehicle:
    def __init__(self, brand, name) -> None:
        self.brand = brand
        self.name = name
        self.__gears = 5

    def __getGearsInfoStr(self):
        return "gears number " + str(self.__gears)
    
    def printInfo(self):
        print(self.brand, self.name, self.__getGearsInfoStr())

vehicle1 = Vehicle("Dodge", "Charger")
vehicle1.printInfo()

# Dostęp do prywatnych pól i metod przez name mangling
print(vehicle1._Vehicle__gears)
print(vehicle1._Vehicle__getGearsInfoStr())


# 📌 PRZYKŁAD 2 – Dziedziczenie i brak dostępu do prywatnych metod

class Car(Vehicle):
    def __init__(self, brand, name) -> None:
        super().__init__(brand, name)
        # print(self.__getGearsInfoStr()) → AttributeError
        print(self._Vehicle__getGearsInfoStr())

car1 = Car("Ford", "Mustang")


# 📌 PRZYKŁAD 3 – Chronione pola i metody (_)

class VehicleProtected:
    def __init__(self, brand, name):
        self.brand = brand
        self.name = name
        self._gears = 5  # chronione pole

    def _get_gears_info_str(self):
        return f"gears number {self._gears}"

    def print_info(self):
        print("Vehicle", self.brand, self.name, self._get_gears_info_str())

class CarProtected(VehicleProtected):
    def __init__(self, brand, name):
        super().__init__(brand, name)
        print("Car", self._get_gears_info_str())

vehicle2 = VehicleProtected("Dodge", "Charger")
vehicle2.print_info()

car2 = CarProtected("Ford", "Mustang")


# ✅ Podsumowanie:
# - __nazwa → prywatne (niedostępne spoza klasy, dostęp przez _ClassName__nazwa)
# - _nazwa → chronione (konwencja: nie używać spoza klasy i jej potomków)
