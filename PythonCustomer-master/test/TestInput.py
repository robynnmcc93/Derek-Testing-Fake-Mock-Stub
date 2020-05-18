from src.Display.Input import Input
from unittest import mock
from unittest.mock import MagicMock
import unittest, csv



class TestInput(unittest.TestCase):

    def testInputInt(self):
        result = self.getInputString = MagicMock(return_value = 4)
        self.assertEqual(4, result)

