from websites import Websites
from client import Client
import os

scriptDir = os.path.dirname(__file__)
os.chdir(scriptDir)

websites = Websites("websites.txt")

from client import dataLock  # przenosimy Lock do client.py

numThreads = 10
threadsList = []

for num in range(numThreads):
    t = Client(f"T{num}", websites, 0.1)
    threadsList.append(t)
    t.start()

for t in threadsList:
    t.join()

websites.saveReport()
print("Job done")
