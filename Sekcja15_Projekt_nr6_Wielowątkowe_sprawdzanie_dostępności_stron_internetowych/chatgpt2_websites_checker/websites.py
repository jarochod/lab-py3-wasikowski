class Websites:
    def __init__(self, filename) -> None:
        self.filename = filename
        self.fileList = [] # lista słowników
        self.reportList = []
        self.index = 0
        self.loadFile(filename)

    def loadFile(self, filename):
        fh = open(filename, "r")
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
            
            # print(data)

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
            print(f"Bad keys in raport: {data}")

    def saveReport(self):
        fh = open("report.txt", "w")

        for el in self.reportList:
            print(el)
            fh.write(f"{el["website"]} - {el}\n")

        fh.close()
        print("Report saved")