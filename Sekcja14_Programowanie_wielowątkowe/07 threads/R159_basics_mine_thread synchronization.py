#R159. Synchronizacja wątków

# Synchronizacja wątków - ma na celu aby w danym momencie wiele wątków nie rywalizowało na dostę
# do zasobu, czyli tylko jeden w danym czasi ebędzie mógł odczytać i zapisać wartość zasobu. 
# Unika się w ten sposób potencjalnych błędów. 
# Python korzysta z prostego mechanizmu blokowania wątków tzw. locking.
# Podstawą jest metoda threading.Lock() zwracająca mechanizm blokujący. Udostępnia metodę 
# acquire( blocking=True ) która zmusza wszystkie wątki aby zaczęły działać synchronicznie dla 
# danego kawałka kodu. 
# Domyślnie opcjonalny parametr blocking ma wartość True co sprawia, że jeśli jakiś wątek pracuje 
# nad danym zasobem to drugi wątek poczeka na swoją kolej. Wartość False sprawi że nie będzie 
# czekał i będzie kontynuował swoją pracę.
# Oprócz acquire() istnieje druga ważna metoda release() która zwalnia blokowanie zasobu, dzięki 
# czemu inny czekający wątek może z niego skorzystać.

"""
import threading, time
data = ["Ola", "Ania", "Kasia", "Daniel", "Adam"]
dataLock = threading.Lock()

class newThread_(threading.Thread):
   
   def __init__(self, threadName, dataLen, sleepTime):
        super().__init__()
        self.threadName = threadName
        self.dataLen = dataLen
        self.sleepTime = sleepTime

   def run(self):
        num = 0
        while num < self.dataLen: 
           
           dataLock.acquire()
           print(self.threadName, data[num]) 
           dataLock.release()
           
           time.sleep(self.sleepTime)
           num += 1 
        print(self.threadName, "ended.")
 
thread1 = newThread_("thread1", len(data), 1)
thread2 = newThread_("thread2", len(data), 1)
thread3 = newThread_("thread3", len(data), 1)

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()
"""



import threading, time  # Importujemy moduły potrzebne do pracy z wątkami i czasem

data = ["Adam", "Ola", "Kasia", "Daniel", "Rafał"]
dataLock = threading.Lock()


# Definicja klasy dziedziczącej po threading.Thread
class someThread_(threading.Thread):
    # Konstruktor klasy – przyjmuje nazwę wątku i czas uśpienia między iteracjami
    def __init__(self, threadName,dataLen, sleepTime) -> None:
        super().__init__()  # Wywołanie konstruktora klasy bazowej
        self.threadName = threadName  # Nazwa wątku (do identyfikacji w wypisach)
        self.dataLen = dataLen
        self.sleepTime = sleepTime  # Czas uśpienia między iteracjami
        

    # Metoda uruchamiana po starcie wątku
    def run(self):
        num = 0  # Licznik iteracji
        max = 6  # Liczba powtórzeń (pętla wykona się 6 razy)
        while num < max:

            dataLock.acquire()
            data[num] = data[num] + " " + str(num)
            localtime = time.localtime()  # Pobranie bieżącego czasu lokalnego
            info = time.strftime("%I:%M:%S", localtime)  # Formatowanie czasu do postaci HH:MM:SS
            print(f"{self.threadName} {info} {data[num]}")  # Wypisanie nazwy wątku i czasu
            dataLock.release()

            time.sleep(self.sleepTime)  # Wstrzymanie działania wątku na określony czas
            num += 1  # Zwiększenie licznika
        print(f"{self.threadName} ended.")  # Wątek zakończył działanie

# Tworzenie trzech instancji klasy wątku z różnymi nazwami i czasami uśpienia
t1 = someThread_("thread1", len(data), 0.5)
t2 = someThread_("thread2", len(data), 0.2)
t3 = someThread_("thread3", len(data), 0.4)

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






"""
print()
import threading, time

data = ["Adam", "Ola", "Kasia", "Daniel", "Rafał"]
dataLock = threading.Lock()

class someThread(threading.Thread):
    def __init__(self, threadName, dataLen, sleepTime):
        threading.Thread.__init__(self)
        self.threadName = threadName
        self.dataLen = dataLen
        self.sleepTime = sleepTime

    def run(self):
        num = 0 
        while num < self.dataLen:

            dataLock.acquire()
            data[num] = data[num] + " " + str(num)
            print( self.threadName, data[num] )
            dataLock.release()

            time.sleep( self.sleepTime )

            num += 1
        print(self.threadName, " ended")


t1 = someThread("T1", len(data) , 0.1)
t2 = someThread("THREAD 2", len(data) , 0.3)
t3 = someThread("thread 3", len(data) , 0.4)

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