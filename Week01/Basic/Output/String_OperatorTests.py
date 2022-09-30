from types import NoneType
from String_Operator import *
import unittest


class MyFirstTests(unittest.TestCase):

    def test_HealtLevals(self):
        # Arrange
        result = HealtLevals("♥")

        # Act

        # Assert
        self.assertEqual(result.health, "♥")

    def test_Health(self):
        # Arrange
        result = Health()

        # Act

        # Assert
        self.assertEqual(result, "♥")
