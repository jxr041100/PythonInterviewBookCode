import unittest
from .context import src

class addBinaryTest(unittest.TestCase):
    def test_AddBinary(self):
        self.assertEqual(src.addBinary("11", "1"), "100")
        self.assertEqual(src.addBinary("1010", "1011"), "10101")
