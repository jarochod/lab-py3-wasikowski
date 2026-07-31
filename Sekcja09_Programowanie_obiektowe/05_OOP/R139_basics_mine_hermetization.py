# R139. Hermetyzacja - enkapsulacja danych w klasie

# OOP w Python - hermetyzacja / enkapsulacja
# metody i zmienne będą prywatne jeśli mają przedrostek z podwójnym podkreśleniem, są tylko
# dostępne w obiekcie na bazie tej klasy.
# 
# Podkreślenia a dostępność:
# - __nazwa → prywatne (name mangling: _ClassName__nazwa)
# - _nazwa → chronione (umowna konwencja) 


class Vehicle:
    def __init__(self, brand, name):
        self.brand = brand
        self.name = name
        self.__gears = 5

    def __getGearsInfoStr(self):
        return "gears number " + str(self.__gears)

    def printInfo(self):
        print(self.brand, self.name, self.__getGearsInfoStr() )


vehicle1 = Vehicle("Dodge", "Charger")
# Próba odwołania do prywatnej zmiennej lub metody powoduje błąd - to jest hermetyzacja.
# print(vehicle1.__gears) # błąd
# vehicle1.__getGearsInfoStr() # błąd
vehicle1.printInfo()
# Dostęp do prywatnych pól i metod przez name mangling (name mangling: _ClassName__nazwa)
print( vehicle1._Vehicle__gears )
print( vehicle1._Vehicle__getGearsInfoStr())


class Car(Vehicle):
    def __init__(self, brand, name):
        Vehicle.__init__(self, brand, name)
        # Klasa pochodna nie ma dostępu do prywatnej.
        # print(self.__gears) # błąd
        # print(self.__getGearsInfoStr()) # bląd
        print(self._Vehicle__getGearsInfoStr())

car1 = Car("Ford", "Mustang")

# ✅ Podsumowanie:
# - __nazwa → prywatne (niedostępne spoza klasy, dostęp przez _ClassName__nazwa)
# - _nazwa → chronione (konwencja: nie używać spoza klasy i jej potomków)