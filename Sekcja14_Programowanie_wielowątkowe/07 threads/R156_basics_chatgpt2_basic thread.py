# R156. Wstęp oraz prosty wątek na bazie _thread

# CHatGPT
# _thread z synchronizacją – wersja z blokadą (lock)”

# Opis lekcji: Synchronizacja wątków z użyciem blokady (lock)
# W tej wersji programu uczymy się, jak unikać konfliktów między wątkami, gdy korzystają one z tych samych zasobów – w tym przypadku funkcji print().

# Ponieważ wszystkie wątki dzielą tę samą pamięć, może się zdarzyć, że dwa wątki jednocześnie spróbują wypisać coś na ekran.
# Efektem może być nieczytelny, przemieszany tekst.

# Aby temu zapobiec, wykorzystujemy blokadę (ang. lock), która pozwala na zabezpieczenie fragmentów kodu tak,
#  aby tylko jeden wątek mógł w danym momencie uzyskać do nich dostęp.

# W module _thread używamy do tego:
# print_lock = _thread.allocate_lock()

# Blokadę można otworzyć i zamknąć przy użyciu metod:
# lock.acquire() – zablokuj dostęp innym wątkom,
# lock.release() – zwolnij dostęp.


import _thread
import time

# Tworzymy globalną blokadę
print_lock = _thread.allocate_lock()   # 🔒 Tworzymy globalny obiekt blokady, który posłuży do zabezpieczania wypisywania na ekran.

def printTime(threadName, sleepTime):
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

# 🧵 Funkcja, która będzie wykonywana w wątku:
# Wypisuje czas 6 razy z przerwami,
# Każdy print() jest chroniony blokadą, aby uniknąć kolizji między wątkami,
# Nawet końcowe "ended" jest chronione tą samą blokadą.


# Startujemy dwa wątki
_thread.start_new_thread(printTime, ("thread 1", 0.5))
_thread.start_new_thread(printTime, ("THREAD 2", 0.3))

# ▶️ Uruchamiamy dwa wątki z różnymi czasami opóźnień (sleepTime), co sprawia, że ich działania się przeplatają.
# ⏳ Główny program „czeka” przez 4 sekundy, żeby wątki mogły spokojnie zakończyć swoje zadania.

# Główna pętla czeka wystarczająco długo, aby wątki się zakończyły
time.sleep(4)


# ✅ Podsumowanie:
# Ta wersja programu pokazuje bezpieczne współdzielenie zasobów przez wątki.

# Dzięki użyciu blokady (lock) unikamy ryzyka, że dwa wątki jednocześnie wypiszą dane na ekran,
# co poprawia czytelność i stabilność programu.

# Choć moduł _thread nadaje się do prostych zastosowań, w większych projektach warto przejść na moduł threading,
# który oferuje więcej funkcji i lepszą strukturę obiektową.
