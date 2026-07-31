# R126. Wstęp do programowania obiektowego - definicja klasy Car

# Programowanie obiektowe w Pythonie
# Python od momentu powstania jest językiem obiektowym – właściwie wszystko w Pythonie jest
# obiektem. Warto więc zadać pytanie: czym tak naprawdę jest programowanie obiektowe?

# Do tej pory operowaliśmy na danych za pomocą programowania proceduralnego, czyli poprzez
# funkcje, do których przekazywane były dane w postaci zmiennych. Funkcje mogły również 
# zwracać wartości.
# W podejściu proceduralnym każdy problem jest rozkładany na etapy i realizowany poprzez 
# wywoływanie funkcji.
# Programowanie obiektowe podchodzi do rozwiązywania problemów w sposób bardziej zorganizowany,
# grupując funkcje oraz dane, które te funkcje obsługują, w jedną całość – obiekty.
# Takie podejście znacząco ułatwia programowanie i jest wręcz niezbędne podczas tworzenia 
# rozbudowanych aplikacji.

# Programowanie obiektowe w Pythonie - definicja klasy 
# Klasa to szablon, na podstawie którego tworzone są obiekty. 
# Definiuje ona zmienne (atrybuty) oraz funkcje (metody), które określają zachowanie obiektu.

# Pierwsza wersja klasy Car (Car1)
class Car1:
    """ Klasa Car1 reprezentuje samochód z określoną marką, modelem i rokiem produkcji. """

    def __init__(self, brand, model, year):
        """
        Konstruktor klasy Car1, inicjalizuje obiekt.
        :param brand: Marka samochodu (np. Ford)
        :param model: Model samochodu (np. Mustang)
        :param year: Rok produkcji
        """
        self.car_name = f"{brand} {model}"
        self.production_date = year

    def print_info(self):
        """ Wyświetla informacje o samochodzie. """
        print(f"{self.car_name} {self.production_date}")

# Tworzenie obiektów na podstawie klasy Car1
mustang1 = Car1("Ford", "Mustang", 1970)
mustang1.print_info()  # Ford Mustang 1970

viper1 = Car1("Dodge", "Viper", 1997)
viper1.print_info()  # Dodge Viper 1997



# Praca z docstring klasy
# Użycie wbudowanej funkcji help()
# help(Car)  # Wyświetli docstring klasy Car
# help(Car.__init__)  # Wyświetli docstring konstruktora
# help(Car.print_info)  # Wyświetli docstring metody print_info

# print(Car.__doc__)  # Docstring klasy Car
# print(Car.__init__.__doc__)  # Docstring konstruktora __init__
# print(Car.print_info.__doc__)  # Docstring metody print_info

"""
Podsumowanie:
help(Car) → Wyświetla pełną dokumentację w formie instrukcji.
Car.__doc__ → Pobiera docstring klasy.
Car.print_info.__doc__ → Pobiera docstring konkretnej metody.
Car? (IPython/Jupyter) → Wyświetla docstring interaktywnie.
Dzięki temu możesz łatwo dokumentować i sprawdzać swoje klasy oraz metody! 
"""


# Druga wersja klasy Car (Car2)
class Car2:
    """ Klasa Car2 rozszerza informacje o samochodzie o kolor i przebieg. """

    def __init__(self, brand, name, color, year):
        """
        Konstruktor klasy Car2, inicjalizuje obiekt.
        :param brand: Marka samochodu (np. Ford)
        :param name: Model samochodu (np. Mustang)
        :param color: Kolor samochodu
        :param year: Rok produkcji
        """
        self.brand = brand
        self.name = name
        self.color = color
        self.year = year
        self.mileage = 1   
        self.set_top_speed(230)
        self.print_info()

    def print_info(self):
        """ Wyświetla informacje o samochodzie. """
        print(self.brand, self.name, self.color, self.year, self.mileage, self.top_speed)

    def set_top_speed(self, new_top_speed):
        """ Ustawia maksymalną prędkość samochodu. """
        self.top_speed = new_top_speed

# Tworzenie obiektów na podstawie klasy Car2
mustang2 = Car2("Ford", "Mustang", "Red", 1970)
mustang2.mileage = 100
mustang2.set_top_speed(235) 
mustang2.print_info()  # Ford Mustang Red 1970 100 235

charger2 = Car2("Dodge", "Charger", "Blue", 1971) 
charger2.set_top_speed(232)
charger2.print_info()  # Dodge Charger Blue 1971 1 232


"""
# Wersja pierwotna z kursu

class Car:
    def __init__(self, brand, name, color, year ):
        self.brand = brand
        self.name = name
        self.color = color
        self.year = year
        self.mileage = 1   
        self.setTopSpeed(230)
        self.printInfo()

    def printInfo(self):
        print(self.brand, self.name, 
            self.color, self.year, self.mileage, self.topSpeed)

    def setTopSpeed(self, newTopSpeed):
        self.topSpeed = newTopSpeed


mustang = Car("Ford", "Mustang", "red", 1970)
mustang.mileage = 100
mustang.setTopSpeed(235) 
mustang.printInfo() 

charger = Car("Dodge", "Charger", "Blue", 1971) 
charger.setTopSpeed(232)
charger.printInfo()"
"""