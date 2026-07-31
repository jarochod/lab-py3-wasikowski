# websites.py
import requests
import validators
import sys

class Websites:
    def __init__(self, filename) -> None:
        self.filename = filename
        self.fileList = []  # lista słowników
        self.reportList = []
        self.index = 0
        self.loadFile(filename)

    def loadFile(self, filename):
        with open(filename, "r") as fh:
            dataList = fh.readlines()

        for v in dataList:
            website = f"https://{v.strip()}"
            statusCode = -1
            index = len(self.fileList)

            data = {
                "website": website,
                "statusCode": statusCode,
                "index": index
            }

            self.fileList.append(data)

    def getNextWebsiteToCheck(self):
        if self.index >= len(self.fileList):
            return None

        data = self.fileList[self.index]
        self.index += 1
        return data

    def putWebsiteData(self, data):
        if "website" in data and "statusCode" in data and "index" in data:
            self.reportList.append(data)
        else:
            print(f"Bad keys in report: {data}")

    def checkUrl(self, data: dict) -> dict:
        try:
            valid = validators.url(data["website"])
            if valid:
                data["validUrlFlag"] = True
                response = requests.get(data["website"], allow_redirects=True)
                data["statusCode"] = response.status_code
            else:
                data["validUrlFlag"] = False
        except Exception:
            data["exception"] = str(sys.exc_info()[0])

        return data

    def saveReport(self):
        with open("report.txt", "w") as fh:
            for el in self.reportList:
                print(el)
                fh.write(f"{el['website']} - {el}\n")
        print("Report saved")
