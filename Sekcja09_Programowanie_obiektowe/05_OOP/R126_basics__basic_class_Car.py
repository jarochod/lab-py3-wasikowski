# R126. Wstęp do programowania obiektowego - definicja klasy Car

# Programowanie obiektowe w Python
# Python od momentu powstania jest językiem obiektowym, właściwie wszystko w Pythonie jest
# obiektem. Warto zadać pytanie, czym tak naprawdę jest programowanie obiektowe?
# Do tej pory operowaliśmy na danych za pomocą programowania proceduralnego, czyli w praktyce
# funkcji, do których były przekazywane dane w postaci zmiennych, mogły również zwracać jakieś
# wartości. Każdy problem jest podzielony na etapy i na wywoływanie funkcji.
#
# Programowanie obiektowe patrzy szerzej na rozwiązywanie problemów, grupując funkcje oraz
# dane, które te funkcje obsługują, w jedną całość, czyli obiekty. Znacząco to ułatwia programowanie,
# wręcz jest niezbędne podczas tworzenia rozbudowanych programów.

# Programowanie obiektowe w Pythonie - definicja klasy 
# Poniżej jest definicja klasy Car, na której podstawie powstają obiekty. Klasa to taki szablon,
# który określa, co powoływany obiekt ma zawierać, np. zmienne oraz metody.


# Wykład - zmieniono Car na Car1, by uniknąć nadpisywania.
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
charger.printInfo()
