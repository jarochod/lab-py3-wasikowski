from websites import *
from url_checker import UrlChecker
import os, sys
import threading, time

scriptDir = os.path.dirname(__file__)
os.chdir(scriptDir)

websites = Websites("websites.txt")
dataLock = threading.Lock()

class Client(threading.Thread):
    def __init__(self, threadName, websites, sleepTime):
        super().__init__()
        self.threadName = threadName
        self.websites = websites
        self.sleepTime = sleepTime

    def run(self):
        while True:
            dataLock.acquire()
            websiteToCheck = self.websites.getNextWebsiteToCheck()
            dataLock.release()

            if not websiteToCheck:
                break

            print(websiteToCheck)
            checkedData = UrlChecker.check(websiteToCheck)

            dataLock.acquire()
            self.websites.putWebsiteData(checkedData)
            dataLock.release()

            time.sleep(self.sleepTime)

        print(f"{self.threadName} ended")


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
