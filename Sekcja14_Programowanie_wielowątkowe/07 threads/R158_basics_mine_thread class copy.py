# R158. Wątek na bazie klasy rozszerzającej Thread

import threading
import time

class MyThread(threading.Thread):
    def __init__(self, name, delay):
        super().__init__()
        self.name = name
        self.delay = delay

    def run(self):
        print(f"[{self.name}] Start in thread: {threading.current_thread().name}")
        time.sleep(self.delay)
        print(f"[{self.name}] End in thread: {threading.current_thread().name}")

# Tworzymy obiekt wątku
t1 = MyThread("Thread1", 1)

print("\nWywołanie t1.run():")
t1.run()  # Uruchamia metodę run(), ale w tym samym (głównym) wątku

print("\nWywołanie t1.start():")
t2 = MyThread("Thread2", 1)
t2.start()  # Uruchamia metodę run() w osobnym wątku

# Oczekujemy na zakończenie drugiego wątku
t2.join()

print("\nKoniec programu")
