#R159. Synchronizacja wątków

import threading, time, traceback, os

scriptDir = os.path.dirname(__file__)
os.chdir(scriptDir)

data = ["Adam", "Ola", "Kasia", "Daniel", "Rafał"]
dataLock = threading.Lock()
counterLock = threading.Lock()

threads_done = 0  # Globalny licznik zakończonych wątków

class someThread_(threading.Thread):
    def __init__(self, threadName, dataLen, sleepTime) -> None:
        super().__init__()
        self.threadName = threadName
        self.dataLen = dataLen
        self.sleepTime = sleepTime

    def run(self):
        global threads_done
        num = 0
        try:
            t= 1 / 0 # 👇 sztuczny wyjątek, żeby przetestować logowanie
            
            while num < self.dataLen:
                with dataLock:
                    data[num] = data[num] + " " + str(num)
                    now = time.strftime("%I:%M:%S", time.localtime())
                    print(f"{self.threadName} {now} {data[num]}")
                time.sleep(self.sleepTime)
                num += 1
        except Exception as e:
            with open("errors.log", "a") as f:
                f.write(f"Error in {self.threadName}:\n")
                traceback.print_exc(file=f)
        finally:
            with counterLock:
                threads_done += 1
                print(f"{self.threadName} ended. Threads done: {threads_done}")

start_time = time.perf_counter()

threads = [
    someThread_(f"thread{i}", len(data), 0.1 + i * 0.1)
    for i in range(1, 16)
]

for t in threads:
    t.start()

print(f"-- {threads[1].threadName} status: {threads[1].is_alive()}")

time.sleep(3)
print(f"-- {threads[1].threadName} status: {threads[1].is_alive()}")

for t in threads:
    t.join()

total_time = time.perf_counter() - start_time
print("All threads ended")
print(f"Total execution time: {total_time:.2f} seconds")



