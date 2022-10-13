import unittest


class StringOperatorTests(unittest.TestCase):

    def test_if_odd_number(self):
        # Arrange
        result = OddNumberCheck(6)

        # Assert
        self.assertEqual(result, False)
