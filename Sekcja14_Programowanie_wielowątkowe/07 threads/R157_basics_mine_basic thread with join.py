# R157. Wątek z funkcji na bazie threading

# threading - również proste wątki na bazie funkcji

# Moduł threading również pozwala na utworzenie wątku z funkcji, ale zwraca obiekt do sterowania wątkiem.
# Funkcja start() rozpoczyna wątek, a join() sprawia, że główny wątek programu poczeka na zakończenie wątku t1. 
# Nieskończona pętla while już nie jest potrzebna.

### Wykład
print("\nWykład")

import threading, time

def printTime_( threadName, sleepTime ):
    num = 0
    max = 6
    while num < max:
        localtime = time.localtime()
        info = time.strftime("%I:%M:%S", localtime)
        print(threadName, info)
        time.sleep(sleepTime)
        num += 1
    print(threadName, "ended.")


t1 = threading.Thread( target = printTime_, args = ("thread1", 0.5) ) # Wątek t1: nazwa "thread1", przerwa 0.5 sekundy
t2 = threading.Thread( target = printTime_, args = ("thread2", 0.2) ) # Wątek t2: nazwa "thread2", przerwa 0.2 sekundy
t3 = threading.Thread( target = printTime_, args = ("thread3", 0.4) ) # Wątek t3: nazwa "thread3", przerwa 0.4 sekundy

t1.start()  # rozpoczyna działanie wątku t1
t2.start()  # rozpoczyna działanie wątku t2
t3.start()  # rozpoczyna działanie wątku t3

t1.join() # join() powoduje, że główny wątek (main thread) czeka, aż t1 się zakończy, zanim przejdzie dalej
print("T1 ended for main thread.") # Wypisujemy info, że t1 się zakończył z punktu widzenia głównego wątku
t2.join() # Czekamy na zakończenie t2
print("T2 ended for main thread.")
t3.join()
print("T3 ended for main thread.")

print("Threads ended.") # Wszystkie wątki się zakończyły – kończymy program

### Wykład - ćwiczenia - wersja z opisami
print("\nWykład - ćwiczenia\n")

# Importujemy potrzebne moduły:
# - threading: do tworzenia i zarządzania wątkami
# - time: do opóźnień (sleep) i pobierania czasu lokalnego

import threading
import time

# Definicja funkcji, która będzie wykonywana w osobnym wątku
def printTime(threadName, sleepTime):
    num = 0           # Licznik iteracji
    max = 6           # Maksymalna liczba powtórzeń (6 razy)

    # Pętla wykona się 6 razy
    while num < max:
        # Pobieramy aktualny czas lokalny
        localTime = time.localtime()
        
        # Wypisujemy nazwę wątku i czas w formacie HH MM SS
        print(threadName, time.strftime("%H %M %S", localTime))

        # Usypiamy wątek na określony czas (np. 0.5 sekundy)
        time.sleep(sleepTime)

        num += 1  # Zwiększamy licznik o 1

    # Gdy pętla się zakończy, wypisujemy informację, że wątek się zakończył
    print(threadName, "ended")

# Tworzymy 3 wątki, każdy uruchomi funkcję printTime z różnymi parametrami

# Wątek t1: nazwa "thread 1", przerwa 0.5 sekundy
t1 = threading.Thread(target=printTime, args=("thread 1", 0.5))

# Wątek t2: nazwa "THREAD 2", przerwa 0.2 sekundy
t2 = threading.Thread(target=printTime, args=("THREAD 2", 0.2))

# Wątek t3: nazwa "T3", przerwa 0.4 sekundy
t3 = threading.Thread(target=printTime, args=("T3", 0.4))

# Uruchamiamy wszystkie 3 wątki
t1.start()
t2.start()
t3.start()

# join() powoduje, że główny wątek (main thread) czeka,
# aż t1 się zakończy, zanim przejdzie dalej
t1.join()
print("T1 ended for main thread")  # Wypisujemy info, że t1 się zakończył z punktu widzenia głównego wątku

# Czekamy na zakończenie t2
t2.join()
print("T2 ended for main thread")

# Czekamy na zakończenie t3
t3.join()
print("T3 ended for main thread")

# Wszystkie wątki się zakończyły – kończymy program
print("Threads ended")


"""
# wersja z kursu, bez opisów

import threading, time

def printTime( threadName, sleepTime ):
    num = 0
    max = 6
    while num < max:
        localTime = time.localtime()

        print(threadName, time.strftime( "%H %M %S" ,localTime))
        time.sleep( sleepTime )

        num += 1
    print(threadName, " ended")

t1 = threading.Thread( target = printTime, args = ("thread 1", 0.5) )
t2 = threading.Thread( target = printTime, args = ("THREAD 2", 0.2) )
t3 = threading.Thread( target = printTime, args = ("T3", 0.4) )

t1.start()
t2.start()
t3.start()

t1.join()
print("T1 ended for main thread")
t2.join()
print("T2 ended for main thread")
t3.join()
print("T3 ended for main thread")

print("Threads ended")

"""
