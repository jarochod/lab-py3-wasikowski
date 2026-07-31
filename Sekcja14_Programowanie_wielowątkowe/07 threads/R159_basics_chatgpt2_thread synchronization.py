#R159. Synchronizacja wątków

import threading, time

data = ["Adam", "Ola", "Kasia", "Daniel", "Rafał"]
dataLock = threading.Lock()

# Klasa wątku – przetwarza listę z zachowaniem synchronizacji
class someThread(threading.Thread):
    def __init__(self, threadName, dataLen, sleepTime) -> None:
        super().__init__()
        self.threadName = threadName  # Nazwa wątku
        self.dataLen = dataLen        # Liczba iteracji (długość danych)
        self.sleepTime = sleepTime    # Czas pauzy między operacjami

    # Główna logika wątku – przetwarza dane i wypisuje status
    def run(self):
        num = 0
        while num < self.dataLen:
            # Blokujemy dostęp do wspólnej listy
            with dataLock:
                data[num] = data[num] + " " + str(num)
                localtime = time.localtime()
                info = time.strftime("%I:%M:%S", localtime)
                print(f"{self.threadName} {info} {data[num]}")
            # Pauza między iteracjami
            time.sleep(self.sleepTime)
            num += 1
        # Wątek zakończył pracę
        print(f"{self.threadName} ended.")

# Start pomiaru czasu
start_time = time.perf_counter()

# Tworzenie wątków z różnym czasem pauzy
threads = [
    someThread(f"thread{i}", len(data), 0.1 + i * 0.1)
    for i in range(1, 16)
]

# Uruchomienie wątków
for t in threads:
    t.start()

# Sprawdzenie statusu thread2
print(f"-- {threads[1].threadName} status: {threads[1].is_alive()}")

time.sleep(3)
print(f"-- {threads[1].threadName} status: {threads[1].is_alive()}")

# Czekamy aż wszystkie wątki zakończą pracę
for t in threads:
    t.join()

# Koniec pomiaru czasu
end_time = time.perf_counter()
total_time = end_time - start_time

print("All threads ended")
print(f"Total execution time: {total_time:.2f} seconds")

