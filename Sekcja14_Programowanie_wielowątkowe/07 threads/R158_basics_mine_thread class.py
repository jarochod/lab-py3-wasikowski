# R158. Wątek na bazie klasy rozszerzającej Thread

# threading - wątek na bazie klasy rozszerzającej Thread

# Klasa tworząca wątek musi dziedziczyć po threading.Thread oraz nadpisać metodę run(),
# która zostanie automatycznie wywołana po uruchomieniu wątku metodą start().
# Dostępne są metody: start() – uruchamia wątek, join() – oczekuje na zakończenie wątku,
# oraz is_alive() – sprawdza, czy wątek nadal działa.


### Wykład
print("\nWykład\n")


import threading, time  # Importujemy moduły potrzebne do pracy z wątkami i czasem

# Definicja klasy dziedziczącej po threading.Thread
class someThread_(threading.Thread):
    # Konstruktor klasy – przyjmuje nazwę wątku i czas uśpienia między iteracjami
    def __init__(self, threadName, sleepTime) -> None:
        super().__init__()  # Wywołanie konstruktora klasy bazowej
        self.threadName = threadName  # Nazwa wątku (do identyfikacji w wypisach)
        self.sleepTime = sleepTime  # Czas uśpienia między iteracjami

    # Metoda uruchamiana po starcie wątku
    def run(self):
        num = 0  # Licznik iteracji
        max = 6  # Liczba powtórzeń (pętla wykona się 6 razy)
        while num < max:
            localtime = time.localtime()  # Pobranie bieżącego czasu lokalnego
            info = time.strftime("%I:%M:%S", localtime)  # Formatowanie czasu do postaci HH:MM:SS
            print(f"{self.threadName} {info}")  # Wypisanie nazwy wątku i czasu
            time.sleep(self.sleepTime)  # Wstrzymanie działania wątku na określony czas
            num += 1  # Zwiększenie licznika
        print(f"{self.threadName} ended.")  # Wątek zakończył działanie

# Tworzenie trzech instancji klasy wątku z różnymi nazwami i czasami uśpienia
t1 = someThread_("thread1", 0.5)
t2 = someThread_("thread2", 0.2)
t3 = someThread_("thread3", 0.4)

# Uruchamianie wszystkich trzech wątków
t1.start()
t2.start()
t3.start()

time.sleep(1)  # Wstrzymanie głównego wątku na 1 sekundę, aby inne wątki zdążyły się uruchomić
print(f"-- Thread 2 status: {t2.is_alive()}")  # Sprawdzenie, czy wątek t2 nadal działa po 1 sekundzie

# Oczekiwanie na zakończenie wątków (blokowanie głównego wątku)
t1.join()
t2.join()
t3.join()

# Wszystkie wątki zakończyły działanie – końcowy komunikat
print("All threads ended")


### Wykład - ćwiczenia
print("\nWykład - ćwiczenia\n")

import threading, time

class someThread(threading.Thread):
    def __init__(self, threadName, sleepTime) -> None:
        super().__init__()
        self.threadName = threadName
        self.sleepTime = sleepTime

    def run(self):
        num = 0
        max = 6
        while num < max:
            localTime = time.localtime()

            print(self.threadName, time.strftime( "%H %M %S" ,localTime))
            time.sleep( self.sleepTime )

            num += 1
        print(self.threadName, " ended")


t1 = someThread("thread 1", 0.5)
t2 = someThread("THREAD 2", 0.2)
t3 = someThread("T3", 0.4)

t1.start()
t2.start()
t3.start()

time.sleep(1)
print( "-- Thread 2 status: ", t2.is_alive() )

t1.join()
t2.join()
t3.join()

print( "-- Thread 2 status: ", t2.is_alive() )
print("All threads ended")


"""
print("\nWykład - ćwiczenia\n")

import threading, time

class someThread(threading.Thread):
    def __init__(self, threadName, sleepTime):
        threading.Thread.__init__(self)
        self.threadName = threadName
        self.sleepTime = sleepTime

    def run(self):
        num = 0
        max = 6
        while num < max:
            localTime = time.localtime()

            print(self.threadName, time.strftime( "%H %M %S" ,localTime))
            time.sleep( self.sleepTime )

            num += 1
        print(self.threadName, " ended")


t1 = someThread("T1", 0.1)
t2 = someThread("THREAD 2", 0.3)
t3 = someThread("thread 3", 0.4)

t1.start()
t2.start()
t3.start()

time.sleep(1)
print( "-- Thread 2 status: ", t2.is_alive() )

t1.join()
t2.join()
t3.join()

print("All threads ended")

"""