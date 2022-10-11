from String_Operator import *
import unittest


class StringOperatorTests(unittest.TestCase):

    def test_healthLevels(self):
        # Arrange
        result = HealthLevels(6, 10, 8)

        # Assert
        self.assertEqual(result.lives, 6)
        self.assertEqual(result.energy, 10)
        self.assertEqual(result.sheild, 8)

    def test_healthStatus(self):
        # Arrange
        result = HealthLevels(7, 11, 9)

        # Assert
        self.assertEqual(result.status["lives"], "♥♥♥♥♥♥♥")
        self.assertEqual(result.status["energy"], "✸✸✸✸✸✸✸✸✸✸✸")
        self.assertEqual(result.status["shield"], "♦♦♦♦♦♦♦♦♦")

    def test_health_icon(self):
        self.assertEqual(set_health_icon("♥", 4), "♥♥♥♥")
        self.assertEqual(set_health_icon("*", 5), "*****")
        self.assertEqual(set_health_icon("♦", 10), "♦♦♦♦♦♦♦♦♦♦")
