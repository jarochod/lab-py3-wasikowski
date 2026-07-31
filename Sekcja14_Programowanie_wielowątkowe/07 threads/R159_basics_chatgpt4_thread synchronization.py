#R159. Synchronizacja wątków

import threading, os
import time
from datetime import datetime

scriptDir = os.path.dirname(__file__)
os.chdir(scriptDir)

lock = threading.Lock()

def log_to_file(text):
    with lock:  # synchronizacja, aby uniknąć problemów przy wielowątkowym zapisie
        with open("threads_output.txt", "a", encoding="utf-8") as f:
            f.write(text + "\n")

def worker(thread_id, user_name):
    for i in range(15):
        timestamp = datetime.now().strftime("%H:%M:%S")
        message = f"thread{thread_id} {timestamp} {user_name} " + " ".join([str(thread_id)] * (i + 1))
        log_to_file(message)
        time.sleep(0.2)

threads = []
users = ["Adam", "Ola", "Kasia", "Daniel", "Rafał"]

for i in range(15):
    t = threading.Thread(target=worker, args=(i + 1, users[i % len(users)]))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

log_to_file("All threads ended")
