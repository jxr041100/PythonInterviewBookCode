import unittest
from .context import src

class fractionToDecimalTest(unittest.TestCase):
    def test_fractionToDecimal(self):
        object = src.FractionToDecimal()
        self.assertEqual(object.fractionToDecimal(1, 2), "0.5")
        self.assertEqual(object.fractionToDecimal(2, 1), "2")
        self.assertEqual(object.fractionToDecimal(2, 3), "0.(6)")
        self.assertEqual(object.fractionToDecimal(4, 333), "0.0(120)")
        self.assertEqual(object.fractionToDecimal(1, 5), "0.2")