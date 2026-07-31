# R98. Określenie dopuszczalnych sposobów przekazywania danych do funkcji dzięki / i *

# parametry przed slash / muszą być przekazane jako argumenty pozycyjne
def printData1(string, number = 10, /):
    print(string, number);

printData1("Test", 5) # Test 5
# printData(string = "Test", number = 11) # błąd, oba muszą być przekazane jako argumenty pozycyjne


# parametry po gwiazdce * muszą być przekazane jako argumenty nazwane
def printData2(*, string, number = 10):
    print(string, number);

printData2(string = "Test", number = 11) # Test 11 # działa prawidłowo
printData2(number = 11, string = "Test") # Test 11 # działa prawidłowo
# printData2("Test", 5) # błąd, oba mają być orzekazane jako argumenty nazwane


# parametry po gwiazdce * muszą być przekazane jako argumenty nazwane
# parametry przed gwiazdką mogą być przekazane jako nazwane albo pozycyjne
def printData3(float, bool, *, string, number = 10):
    print(float, bool, string, number);

printData3(12.5, bool=True, string="Test", number=11) # 12.5 True Test 11
printData3(float=12.5, bool=False, number=11, string="Test") # 12.5 False Test 11
printData3(20.3, False, number=11, string="Test") # 20.3 False Test 11


def printCar(brand, / , name = "concept", * , year = 1960, color = "black"):
    print(brand, name, year, color)


# printCar( brand = "Ford", "Mustang", color = "blue", year = 1973) # błąd
printCar("Ford", "Mustang", year = 1973, color="blue")
printCar( "Ford", name = "Mustang", color = "blue", year = 1973)
# printCar( "Ford", name = "Mustang", "blue", year = 1973) # błąd
