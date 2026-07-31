# 🔒 Hermetyzacja (enkapsulacja) w Pythonie
# To jeden z filarów programowania obiektowego (OOP). Polega na ukrywaniu wewnętrznego stanu obiektu przed światem zewnętrznym,
# a dostęp do tych danych odbywa się przez kontrolowane metody (czyli właśnie gettery i settery).
# 
# W Pythonie nie ma typowego modyfikatora private, jak w np. Javie, ale przyjęło się, że:
# self._zmienna → oznacza, że to zmienna chroniona (powinna być traktowana jako "wewnętrzna"),
# self.__zmienna → to zmienna prywatna, Python dodatkowo ją „name-mangluje”, co utrudnia dostęp z zewnątrz.


# 💡 Dlaczego to jest dobre?
# 1. Bezpieczeństwo: nie pozwalamy użytkownikowi klasy ustawić np. -5 biegów.
# 2. Czytelność: vehicle.gears = 5 wygląda jak zwykła właściwość, ale działa jak funkcja.
# 3. Elastyczność: w przyszłości getter lub setter mogą np. logować zmiany, synchronizować z bazą danych, obliczać coś dynamicznie.


# Przykklad 1

class Person:
    def __init__(self, name):
        print(f"🛠️ Utworzebue instancji 'p' klasy Person z name '{name}'")
        self._name = name

    @property
    def name(self):
        print("🔍 Getter: pobieranie wartości name")
        return self._name

    @name.setter
    def name(self, value):
        print(f"🛠️ Setter: ustawianie wartości name na '{value}'")
        if not value:
            raise ValueError("❌ Imię nie może być puste!")
        self._name = value

# 🔽 Użycie
p = Person("Ola")

# Getter
print(p.name)      # 🔍 + wynik

# Setter
p.name = "Ania"    # 🛠️

# Getter znowu
print(p.name)


## Przykład 2

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._celsius = float(value)

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (float(value) - 32) * 5 / 9

# 🔽 Użycie
t = Temperature(25)
print(f"{t.celsius} °C")        # 25.0 °C
print(f"{t.fahrenheit} °F")     # 77.0 °F

t.fahrenheit = 98.6
print(f"{t.celsius:.2f} °C")    # 37.00 °C


# Przykład 3

class Car:
    def __init__(self):
        self.__gears = 5
        self.__speed = 0
        self.__brand = "Generic"

    # gears - liczba biegów
    @property
    def gears(self):
        return self.__gears

    @gears.setter
    def gears(self, value):
        if value > 0:
            self.__gears = value

    # speed - prędkość
    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if 0 <= value <= 300:
            self.__speed = value

    # brand - marka samochodu
    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        if isinstance(value, str) and value.strip():
            self.__brand = value

    # pomocnicza metoda do wypisania stanu auta
    def show_info(self):
        print(f"Brand: {self.__brand}, Gears: {self.__gears}, Speed: {self.__speed} km/h")

# 🔽 Użycie
car = Car()
car.show_info()                # Brand: Generic, Gears: 5, Speed: 0 km/h

car.gears = 6
car.speed = 120
car.brand = "Toyota"

print(car.gears)               # 6
print(car.speed)               # 120
print(car.brand)               # Toyota

car.show_info()                # Brand: Toyota, Gears: 6, Speed: 120 km/h

# Próba ustawienia błędnych wartości
car.gears = -1                 # zignorowane
car.speed = 999                # zignorowane
car.brand = ""                 # zignorowane

car.show_info()                # Wartości się nie zmieniły
