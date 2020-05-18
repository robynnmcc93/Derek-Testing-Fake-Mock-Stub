class ReadFromStub:

    def getFileData(self):

        fileData = []
        fileData.append(["emailAddress,firstName,lastName,password"])
        fileData.append(["2483898m@student.gla.ac.uk,Robynn,McCrossan,4567"])
        fileData.append(["example@googlemail.com,John,Smith,1234"])
        fileData.append(["anotherexample@hotmail.com,Karen,Jones,2345"])

        return fileData

