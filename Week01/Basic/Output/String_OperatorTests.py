from types import NoneType
from String_Operator import *
import unittest


class MyFirstTests(unittest.TestCase):

    def test_healthLevels(self):
        # result = HealthLevels(6,10.8)
        # Arrange
        result = HealthLevels()

        # Assert
        self.assertEqual(result.lives, 6)
        self.assertEqual(result.energy, 9)
        self.assertEqual(result.sheild, 15)

    def test_healthStatus(self):
        # result = HealthLevels(6,10.8)
        # Arrange
        result = HealthLevels()

        # Assert
        self.assertEqual(result.status["lives"], "♥♥♥♥♥♥")
        self.assertEqual(result.status["energy"], "***********")
        self.assertEqual(result.status["sheild"], "♦♦♦♦♦♦♦♦♦")

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
