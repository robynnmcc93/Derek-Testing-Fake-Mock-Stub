import unittest
from src.DataSource.ReadCSVFile import ReadCSVFile

from EntitiesDatabaseMapping.CustomerDatabaseFake import getData
from EntitiesDatabaseMapping.CustomerDatabaseMapping import CustomerDatabaseMapping
from EntitiesDatabaseMapping import CustomerDatabaseFake


class TestCustomerDatabaseMapping(unittest.TestCase):

    def test_getCustomerDataFromFile(self):
        readCSVFile = ReadCSVFile()
        customerDatabaseMapping = CustomerDatabaseMapping()
        customerData = customerDatabaseMapping.getCustomerDataFromFile()
        self.assertEqual( customerData[0] ,['derek.somerville@glasgow.ac.uk', 'Derek', 'Somerville', '1234'])

    def test_getCustomerDataFromDatabase(self):
        customerDatabaseMapping = CustomerDatabaseMapping()
        customerData = customerDatabaseMapping.getCustomerData()
        self.assertEqual( customerData[0] ,('derek.somerville@glasgow.ac.uk', 'Derek', 'Somerville', '1234'))


    def testGetCustomerDataFromFake(self):

        customerData = CustomerDatabaseFake(getData(self))
        self.assertEqual(customerData, ['2483898m@student.glasgow.ac.uk', 'Robynn', 'McCrossan', '1234', ['blah@google.com', 'Scott', 'McCrone', '4321']])


def main():
    unittest.main()

if __name__ == "__main__":
    unittest.main()
