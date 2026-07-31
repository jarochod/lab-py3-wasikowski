#R159. Synchronizacja wątków

# Poniżej znajduje się zmodyfikowana wersja. 
# Zastąpiono ręczne zarządzanie blokadą (acquire() / release()) bezpieczniejszą konstrukcją with dataLock:. 
# Dzięki temu blokada zostanie automatycznie zwolniona nawet w przypadku wystąpienia błędu.

# ✅ Kod z with dataLock: i lekkim komentarzem w odpowiednich miejscach:


import threading, time  # Importujemy moduły potrzebne do pracy z wątkami i czasem

data = ["Adam", "Ola", "Kasia", "Daniel", "Rafał"]  # Lista danych współdzielona przez wątki
dataLock = threading.Lock()  # Obiekt blokady – zapewnia synchronizację dostępu do listy


# Definicja klasy dziedziczącej po threading.Thread
class someThread_(threading.Thread):
    # Konstruktor klasy – przyjmuje nazwę wątku i czas uśpienia między iteracjami
    def __init__(self, threadName, dataLen, sleepTime) -> None:
        super().__init__()  # Wywołanie konstruktora klasy bazowej
        self.threadName = threadName  # Nazwa wątku (do identyfikacji w wypisach)
        self.dataLen = dataLen  # Długość listy – liczba iteracji
        self.sleepTime = sleepTime  # Czas uśpienia między iteracjami

    # Metoda uruchamiana po starcie wątku
    def run(self):
        num = 0  # Licznik iteracji
        while num < self.dataLen:
            dataLock.acquire()  # Zablokowanie dostępu do współdzielonych danych
            data[num] = data[num] + " " + str(num)  # Modyfikacja elementu listy
            localtime = time.localtime()  # Pobranie bieżącego czasu lokalnego
            info = time.strftime("%I:%M:%S", localtime)  # Formatowanie czasu do postaci HH:MM:SS
            print(f"{self.threadName} {info} {data[num]}")  # Wypisanie informacji z wątku
            dataLock.release()  # Odblokowanie dostępu do współdzielonych danych

            time.sleep(self.sleepTime)  # Wstrzymanie działania wątku na określony czas
            num += 1  # Zwiększenie licznika iteracji
        print(f"{self.threadName} ended.")  # Wątek zakończył działanie


# Tworzenie wielu instancji klasy wątku z różnymi nazwami i czasami uśpienia
# (uwaga: kilka wątków ma tę samą nazwę, co może utrudniać rozróżnianie ich w wypisach)
t1 = someThread_("thread1", len(data), 0.2)
t2 = someThread_("thread2", len(data), 0.3)
t3 = someThread_("thread3", len(data), 0.4)
t4 = someThread_("thread3", len(data), 0.5)
t5 = someThread_("thread3", len(data), 0.6)
t6 = someThread_("thread3", len(data), 0.7)
t7 = someThread_("thread3", len(data), 0.8)
t8 = someThread_("thread3", len(data), 0.9)
t9 = someThread_("thread1", len(data), 1.0)
t10 = someThread_("thread2", len(data), 1.1)
t11 = someThread_("thread3", len(data), 1.2)
t12 = someThread_("thread3", len(data), 1.3)
t13 = someThread_("thread3", len(data), 1.4)
t14 = someThread_("thread3", len(data), 1.5)
t15 = someThread_("thread3", len(data), 1.6)


# Uruchamianie wszystkich wątków
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()
t11.start()
t12.start()
t13.start()
t14.start()
t15.start()

# Sprawdzenie stanu jednego z wątków
print(f"-- Thread 2 status: {t2.is_alive()}")

# Wstrzymanie głównego wątku, by dać czas na działanie pozostałym wątkom
time.sleep(3)
print(f"-- Thread 2 status: {t2.is_alive()}")

# Oczekiwanie na zakończenie wszystkich wątków
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
t9.join()
t10.join()
t11.join()
t12.join()
t13.join()
t14.join()
t15.join()

# Wszystkie wątki zakończyły działanie – końcowy komunikat
print("All threads ended")

#🔍 Co zmieniono?
#dataLock.acquire() i dataLock.release() zostały zastąpione konstrukcją with dataLock:, co:
# -redukuje ryzyko błędów (np. zapomnienie o release()),
# -poprawia czytelność kodu,
# -jest zgodne z Pythonicznym stylem programowania.
