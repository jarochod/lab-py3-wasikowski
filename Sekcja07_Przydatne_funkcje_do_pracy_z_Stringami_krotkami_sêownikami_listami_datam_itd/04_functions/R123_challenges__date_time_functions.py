# R123. Przydatne funkcje do operacji na datach - zadanie
# 
# Zadanie - śledzenie czasu pracy nad projektem
# W tym zadaniu użyjesz modułów time i datetime do symulacji prostego systemu śledzenia
# czasu pracy nad projektem. Nauczysz się używać różnych funkcji związanych z czasem i datą.
# 
# 1) Użyj modułu datetime, aby zapisać czas rozpoczęcia pracy nad projektem jako
# zmienną 'start_time'.
# 2) Symuluj pracę nad projektem poprzez wywołanie time.sleep() z losowo wybranym
# krótkim czasem (np. od 1 do 5 sekund).
# 3) Użyj modułu datetime ponownie, aby zapisać czas zakończenia pracy nad projektem
# jako zmienną 'end_time'.
# 4) Oblicz łączny czas pracy nad projektem przez odjęcie 'start_time' od 'end_time' i
# wyświetl wynik.
# 5) Jeśli łączny czas pracy przekracza 3 sekundy, wyświetl komunikat o dużej ilości
# włożonego czasu, w przeciwnym razie powinformuj o krótkim czasie pracy.

import datetime
import time
import random

# 1) 
start_time = datetime.datetime.now() # czas rozpoczęcia pracy nad projektem
print("Czas rozpoczęcia zadania:",start_time.strftime("%H:%M:%S %d.%m.%Y"))

# 2) symulacja pracy 
sleep_time = random.randint(1, 5) # losowo wybrany czas od 1 do 5 sekund
time.sleep(sleep_time) # symulacja pracy

# 3) 
end_time = datetime.datetime.now() # czas zakończenia pracy nad projektem
print("Czas zakończenia zadania:",end_time.strftime("%H:%M:%S %d.%m.%Y"))

# 4)
total_work_time = end_time - start_time # łączny czas pracy nad projektem
print("Czas pracy:",total_work_time)

# 5)
if total_work_time.total_seconds() > 3: # Jeśli łączny czas pracy przekracza 3 sekundy
    print("Duża ilości włożonego czasu.")
else:
    print("Krótki czas pracy nad projektem.")