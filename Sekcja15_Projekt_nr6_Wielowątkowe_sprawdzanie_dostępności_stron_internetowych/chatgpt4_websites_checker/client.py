import threading
import time
from config import dataLock
from url_checker import UrlChecker

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
