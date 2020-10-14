import unittest
from .context import src

class nextPermutationTest(unittest.TestCase):
    def test_nextPermutation(self):
        self.assertEqual(src.NextPermutation.nextPermutation(self,[1,2,3]), [1,3,2])
        self.assertEqual(src.NextPermutation.nextPermutation(self,[3,2,1]), [1,2,3])
        self.assertEqual(src.NextPermutation.nextPermutation(self,[1,1,5]), [1,5,1])
        self.assertEqual(src.NextPermutation.nextPermutation(self,[1]), [1])