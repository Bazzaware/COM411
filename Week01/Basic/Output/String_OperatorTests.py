from types import NoneType
from String_Operator import *
import unittest


class MyFirstTests(unittest.TestCase):

    def test_healtLevels(self):
        # Arrange
        result = HealtLevels("♥")

        # Act

        # Assert
        self.assertEqual(result.health, "♥")

    def test_health(self):
        # Arrange
        result = health()

        # Act

        # Assert
        self.assertEqual(result, "♥")
