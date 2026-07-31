# R156. Wstęp oraz prosty wątek na bazie _thread

# Wątki - pozwalają na podział programu na kilka równolegle działających części co daje możliwość 
# przyśpieszenia jego działania na procesorach z wieloma rdzeniami. 
# Wątki powstałe w programie dzielą się dostępem do pamięci oraz zasobów co wymaga odpowiedniego 
# zarządzania zwanego synchronizacją aby ustrzec się przed potencjalnymi błędami, Przykładowo kiedy 
# jeden wątek zapisuje wartość do zmiennej w momencie, gdy inny wątek próbuje ją odczytać co może się 
# skończyć błędną wartością.
#  Python  daje nam do użytku dwa moduły na pracę z wątkami:  
#   _thread - nisko poziomowe api
#   threading - wysoko poziomowe api


# Funkcja printTime będzie wątkiem powołanym do życia dzięki funkcji _thread.start_new_thread() przyjmującej 
# funkcję jako wątek oraz krotkę argumentów przekazywanych tej funkcji. Rozpoczęcie wątku powoduje 
# od razu dalsze wykonanie programu, dlatego aby się nie zakończył potrzebna jest nieskończona pętla while.
#           time.sleep(x) usypia wątek na x sekund np. 0.5


# _thread - proste wątki na bazie funkcji

### Wykład
print("\nWykład\n")

import _thread, time
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

_thread.start_new_thread( printTime_, ("BASIC thread", 1) )
_thread.start_new_thread( printTime_, ("Another thread", 2) )

# while 1 == 1:
#     pass
time.sleep(15)


### Wykład - ćwiczenia
print("\nWykład - ćwiczenia\n")

import _thread, time

def printTime( threadName, sleepTime ):
    num = 0
    max = 6
    while num < max:
        localTime = time.localtime()

        print(threadName, time.strftime( "%H %M %S" ,localTime))
        time.sleep( sleepTime )

        num += 1
    print(threadName, " ended")

_thread.start_new_thread( printTime, ("thread 1", 0.5) )
_thread.start_new_thread( printTime, ("THREAD 2", 0.3) )

time.sleep(4)




print("\nWykład - wersja chatgpt\n")
# Wersja z opisami i globalną blokadą

import _thread, time

# Tworzymy globalną blokadę
print_lock = _thread.allocate_lock()

def printTime2(threadName, sleepTime):
    num = 0
    max_count = 6
    while num < max_count:
        localTime = time.localtime()

        # Używamy blokady przy print
        print_lock.acquire()
        try:
            print(threadName, time.strftime("%H %M %S", localTime))
        finally:
            print_lock.release()

        time.sleep(sleepTime)
        num += 1

    # Również zabezpieczamy ostatni print
    print_lock.acquire()
    try:
        print(threadName, "ended")
    finally:
        print_lock.release()

# Startujemy dwa wątki
_thread.start_new_thread(printTime2, ("thread 1", 0.5))
_thread.start_new_thread(printTime2, ("THREAD 2", 0.3))

# Główna pętla czeka wystarczająco długo, aby wątki się zakończyły
time.sleep(4)
