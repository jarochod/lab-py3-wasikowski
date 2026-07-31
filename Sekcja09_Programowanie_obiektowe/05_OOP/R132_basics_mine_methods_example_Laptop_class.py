# R132. Metody klasy

# Wewnątrz definicji klasy można zdefiniować metody, czyli funkcje, które są częścią klasy.
# Metody można wywołać wewnątrz innych metod klasy, korzystając z `self`, np. `self.get_full_name()`.
# Poza klasą metody wywołujemy na rzecz konkretnego obiektu, np. `person1.get_full_name()`.



class Person:
    """Reprezentuje osobę z imieniem, nazwiskiem i krajem pochodzenia."""
    
    def __init__(self, name, surname, country) -> None:
        """Inicjalizuje obiekt klasy Person, przypisując imię, nazwisko i kraj."""
        self.name = name
        self.surname = surname
        self.country = country
    
    def get_full_name(self):
        """Zwraca pełne imię i nazwisko osoby."""
        return f"{self.name} {self.surname}"
    
    def print_data(self):
        """Wypisuje pełne imię i nazwisko oraz kraj pochodzenia."""
        print(f"{self.get_full_name()} - {self.country}")

# Tworzenie obiektu klasy Person
person1 = Person("Ola", "Kowalska", "Polska")

# Dostęp do atrybutów obiektu
print(person1.name)
print(person1.surname)

# Wywołanie metod obiektu
print(f"Full name: {person1.get_full_name()}")
person1.print_data()


print("\nWykład - ćwiczenia")

class Laptop:
    def __init__(self, cpu, ram=4096, gpu="AMD", price=2000) -> None:
        self.setCpu(cpu)
        self.setRam(ram)
        self.gpu = gpu
        self.price = price
    
    def setCpu(self, cpu):
        valid_cpus = {"amd", "intel", "arm"}
        self.cpu = cpu if isinstance(cpu, str) and cpu.lower() in valid_cpus else "unknown"

    def setRam(self, ram):
        if isinstance(ram, int) and ram >= 4096:
        # if type(ram) == int and ram >= 4096:  
            self.ram = ram
        else:
            print("Nieprawidłowe dane RAM. Ustawiono domyślną wartość 4096 MB.")
            self.ram = 4096

    def printData(self):
        print(f"CPU: {self.cpu}, RAM: {self.ram} MB, GPU: {self.gpu}, Cena: {self.price} PLN")

# Testy
laptop1 = Laptop("AMD", 4, "AMD", 2000)  # Błąd w RAM, powinno się ustawić 4096
laptop1.printData()

laptop2 = Laptop("x")  # Nieznany CPU, RAM domyślny 4096
laptop2.printData()

laptop3 = Laptop("Intel", 8192)  # Poprawne dane
laptop3.printData()

laptop4 = Laptop("ARM", -2048)  # Błąd w RAM, zostanie ustawione 4096
laptop4.printData()


"""
print("\nWykład - ćwiczenia")

class Laptop:
    def __init__(self, cpu, ram = 4096, gpu = "AMD", price = 2000):
        self.setCpu(cpu)
        self.setRam(ram)
        self.gpu = gpu
        self.price = price

    def setCpu(self, cpu):
        if cpu.lower() == "amd" or cpu.lower() == "intel" or cpu.lower() == "arm":
            self.cpu = cpu
        else:
            self.cpu = "unknown"

    def setRam(self, ram): 
        if type(ram) == int and ram >= 2048:
            self.ram = ram
        else:
            self.ram = 2048

    def printData(self):
        print(self.cpu, self.ram, self.gpu, self.price)


laptop1 = Laptop("Intel", 16000)
laptop1.printData()

laptop2 = Laptop("AMD", 32000)
laptop2.printData() 
"""