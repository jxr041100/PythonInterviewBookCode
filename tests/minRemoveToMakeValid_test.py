import unittest
from .context import src

class minRemoveToMakeValidTest(unittest.TestCase):
    def test_minRemoveToMakeValid(self):
        object = src.MinRemoveToMakeValid()
        self.assertEqual(object.minRemoveToMakeValid("lee(t(c)o)de)"), "lee(t(c)o)de")
        self.assertEqual(object.minRemoveToMakeValid("a)b(c)d"), "ab(c)d")
        self.assertEqual(object.minRemoveToMakeValid("))(("), "")
