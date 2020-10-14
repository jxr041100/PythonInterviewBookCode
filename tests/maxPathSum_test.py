import unittest
from .context import src

class maxPathSumTest(unittest.TestCase):
    def test_maxPathSum1(self):
        root = src.TreeNode(1)
        root.left = src.TreeNode(2)
        root.right = src.TreeNode(3)
        self.assertEqual(src.maxPathSum(root), 6)

    def test_maxPathSum2(self):
        root = src.TreeNode(-10)
        root.left = src.TreeNode(9)
        root.right = src.TreeNode(20)
        root.right.left = src.TreeNode(15)
        root.right.right = src.TreeNode(7)
        self.assertEqual(src.maxPathSum(root), 42)
