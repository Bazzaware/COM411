from types import NoneType
from String_Operator import *
import unittest


class MyFirstTests(unittest.TestCase):

    def test_healthLevels(self):
        # result = HealthLevels(6,10.8)
        # Arrange
        result = HealthLevels()

        # Assert
        self.assertEqual(result.lives, "♥♥♥♥♥♥")
        self.assertEqual(result.energy, "***********")
        self.assertEqual(result.sheild, "♦♦♦♦♦♦♦♦♦")

    def test_health(self):
        # Arrange
        result = health()

        # Act

        # Assert
        self.assertEqual(result, "♥")

    def test_health_icon(self):
        self.assertEqual(set_health_icon("♥", 4), "♥♥♥♥")
        self.assertEqual(set_health_icon("*", 5), "*****")
        self.assertEqual(set_health_icon("♦", 10), "♦♦♦♦♦♦♦♦♦♦")
