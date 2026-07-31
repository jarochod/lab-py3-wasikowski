import threading, time, traceback, os

scriptDir = os.path.dirname(__file__)
os.chdir(scriptDir)

data = ["Adam", "Ola", "Kasia", "Daniel", "Rafał"]
dataLock = threading.Lock()
counterLock = threading.Lock()
lock = threading.Lock()  # Lock do synchronizacji logowania

threads_done = 0  # Globalny licznik zakończonych wątków

def log_to_file(file_name, text):
    with lock:  # synchronizacja przy wielowątkowym zapisie
        with open(file_name, "a", encoding="utf-8") as f:
            f.write(text + "\n")

def log_and_print(text, file_name="threads_output.txt"):
    print(text)
    log_to_file(file_name, text)

class someThread(threading.Thread):
    def __init__(self, threadName, dataLen, sleepTime) -> None:
        super().__init__()
        self.threadName = threadName
        self.dataLen = dataLen
        self.sleepTime = sleepTime

    def run(self):
        global threads_done
        num = 0
        try:
            # t = 1 / 0  # 👇 sztuczny wyjątek, żeby przetestować logowanie

            while num < self.dataLen:
                with dataLock:
                    data[num] = data[num] + " " + str(num)
                    now = time.strftime("%I:%M:%S", time.localtime())
                    log_and_print(f"{self.threadName} {now} {data[num]}")
                time.sleep(self.sleepTime)
                num += 1
        except Exception as e:
            error_message = f"Error in {self.threadName}:\n" + traceback.format_exc()
            log_to_file("errors.log", error_message)
        finally:
            with counterLock:
                threads_done += 1
                log_and_print(f"{self.threadName} ended. Threads done: {threads_done}")

start_time = time.perf_counter()

threads = [
    someThread(f"thread{i}", len(data), 0.1 + i * 0.1)
    for i in range(1, 16)
]

for t in threads:
    t.start()

log_and_print(f"-- {threads[1].threadName} status: {threads[1].is_alive()}")

time.sleep(3)
log_and_print(f"-- {threads[1].threadName} status: {threads[1].is_alive()}")

for t in threads:
    t.join()

total_time = time.perf_counter() - start_time
log_and_print("All threads ended")
log_and_print(f"Total execution time: {total_time:.2f} seconds")
