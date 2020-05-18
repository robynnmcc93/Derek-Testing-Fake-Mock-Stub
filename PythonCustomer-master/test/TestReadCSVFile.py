import unittest, csv
from unittest import mock
from unittest.mock import MagicMock
from src.DataSource.ReadCSVFile import ReadCSVFile
from src.DataSource.DataSourceConstants import *

from src.DataSource.ReadFromStub import ReadFromStub

class TestReadCSVFile(unittest.TestCase):

    readCSVFile = ReadCSVFile()

    def test_getCustomerDataFromFile(self):
        fileData = self.readCSVFile.getFileData(ENTITIES_FOLDER,"customer" + ".csv")
        self.assertEqual( fileData[1] ,['derek.somerville@glasgow.ac.uk', 'Derek', 'Somerville', '1234'])

    def test_getLastLinesFromFile(self):
        fileLines = self.readCSVFile.getLastLines( ENTITIES_FOLDER, "customer" + ".csv",1)
        self.assertEqual( fileLines ,['matthew.barr@glasgow.ac.uk', 'Matt', 'Barr', '4321'])

    def test_getCustomerDataFromStub(self):
        fileData = ReadFromStub.getFileData(self)
        self.assertEqual (fileData[1] ,["2483898m@student.gla.ac.uk,Robynn,McCrossan,4567"])


    def test_getCustomerDataFake(self):
        fileData = []
        fileData.append(["emailAddress,firstName,lastName,password"])
        fileData.append(["2483898m@student.gla.ac.uk,Robynn,McCrossan,4567"])
        fileData.append(["example@googlemail.com,John,Smith,1234"])
        fileData.append(["anotherexample@hotmail.com,Karen,Jones,2345"])

        self.assertEqual(["emailAddress,firstName,lastName,password"], fileData[0])


    


def main():
    unittest.main()

if __name__ == "__main__":
    unittest.main()

