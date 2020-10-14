import unittest
from .context import src

class isNumberTest(unittest.TestCase):
    def test_isNumber(self):
        object = src.IsNumber() # instance the class
        self.assertEqual(object.isNumber("0"), True)
        self.assertEqual(object.isNumber("0.1"), True)
        self.assertEqual(object.isNumber("abc"), False)
        self.assertEqual(object.isNumber("1 a"), False)
        self.assertEqual(object.isNumber("2e10"), True)
        self.assertEqual(object.isNumber("-90e3"), True)
        self.assertEqual(object.isNumber("1e"), False)
        self.assertEqual(object.isNumber("e3"), False)
        self.assertEqual(object.isNumber("6e-1"), True)
        self.assertEqual(object.isNumber("99e2.5"), False)
        self.assertEqual(object.isNumber("--6"), False)
        self.assertEqual(object.isNumber("-+3"), False)
        self.assertEqual(object.isNumber("99a54e53"), False)