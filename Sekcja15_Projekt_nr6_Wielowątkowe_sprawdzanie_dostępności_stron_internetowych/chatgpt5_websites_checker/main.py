# from pack.websites import Websites
# from pack.client import Client
# from pack.config import dataLock
from pack import Client, Websites #, dataLock
import os

scriptDir = os.path.dirname(__file__)
os.chdir(scriptDir)

websites = Websites("websites.txt")

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
