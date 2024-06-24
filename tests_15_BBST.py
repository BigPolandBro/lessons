# questions:
# 1) что делать если массив на входе [2, 2, 2, 2, 2, 2, 2] - алгоритм выбора центрального не работает в таком случае

import unittest
import itertools
import random

class TestBalancedBST(unittest.TestCase):
    
    def setUp(self):
        self.tree = BalancedBST()
        
    def test_balanced_search(self):
        n0 = BSTNode(5, None)
        n10 = BSTNode(4, n0)
        n11 = BSTNode(5, n0)
        n20 = BSTNode(2, n10)
        n21 = BSTNode(4, n10)
        n30 = BSTNode(1, n20)
        n0.LeftChild = n10
        n0.RightChild = n11
        n10.LeftChild = n20
        n10.RightChild = n21
        n20.LeftChild = n30
        
        self.tree.Root = n0
        
        self.assertFalse(self.tree.IsBalanced(n0))
        self.assertTrue(self.tree.IsBalanced(n10))
        self.assertTrue(self.tree.IsBalanced(n11))
        self.assertTrue(self.tree.IsBalanced(n20))
        self.assertTrue(self.tree.IsBalanced(n21))
        self.assertTrue(self.tree.IsBalanced(n30))
        
        self.assertTrue(self.tree.IsSearch(n0))
        self.assertTrue(self.tree.IsSearch(n10))
        self.assertTrue(self.tree.IsSearch(n11))
        self.assertTrue(self.tree.IsSearch(n20))
        self.assertTrue(self.tree.IsSearch(n21))
        self.assertTrue(self.tree.IsSearch(n30))
        
        n21.NodeKey = 3
        self.assertFalse(self.tree.IsSearch(n0))
        self.assertFalse(self.tree.IsSearch(n10))
        self.assertTrue(self.tree.IsSearch(n11))
        self.assertTrue(self.tree.IsSearch(n20))
        self.assertTrue(self.tree.IsSearch(n21))
        self.assertTrue(self.tree.IsSearch(n30))
    
    def test_empty(self):
        a = []
        self.tree.GenerateTree(a)
        
        self.assertEqual(self.tree.TraverseTree(), [])
        self.assertTrue(self.tree.IsBalanced(self.tree.Root))
        self.assertTrue(self.tree.IsSearch(self.tree.Root))
    
    def test_one(self):
        a = [404]
        res = [[0, 404]]
        self.tree.GenerateTree(a)
        
        self.assertEqual(self.tree.TraverseTree(), res)
        self.assertTrue(self.tree.IsBalanced(self.tree.Root))
        self.assertTrue(self.tree.IsSearch(self.tree.Root))
        
    def test_two(self):
        a = [404, 101]
        res = [[0, 101], [1, 404]]
        self.tree.GenerateTree(a)
        
        self.assertEqual(self.tree.TraverseTree(), res)
        self.assertTrue(self.tree.IsBalanced(self.tree.Root))
        self.assertTrue(self.tree.IsSearch(self.tree.Root))
    
    def test_three_int(self):
        a = [1, 404, 1001]
        res = [[0, 404], [1, 1], [1, 1001]]
        permutations = [list(perm) for perm in itertools.permutations(a)]

        for perm in permutations:
            self.tree.GenerateTree(perm)
            self.assertEqual(self.tree.TraverseTree(), res)
            self.assertTrue(self.tree.IsBalanced(self.tree.Root))
            self.assertTrue(self.tree.IsSearch(self.tree.Root))
            
    def test_five_int(self):
        a = [3, 7, 13, 17, 23]
        res = [[0, 13], [1, 3], [1, 17], [2, 7], [2, 23]]
        permutations = [list(perm) for perm in itertools.permutations(a)]

        for perm in permutations:
            self.tree.GenerateTree(perm)
            self.assertEqual(self.tree.TraverseTree(), res)
            self.assertTrue(self.tree.IsBalanced(self.tree.Root))
            self.assertTrue(self.tree.IsSearch(self.tree.Root))
            
    def test_six_int(self):
        a = [3, 7, 13, 17, 23, 25]
        res = [[0, 13], [1, 3], [1, 23], [2, 7], [2, 17], [2, 25]]
        permutations = [list(perm) for perm in itertools.permutations(a)]

        for perm in permutations:
            self.tree.GenerateTree(perm)
            self.assertEqual(self.tree.TraverseTree(), res)
            self.assertTrue(self.tree.IsBalanced(self.tree.Root))
            self.assertTrue(self.tree.IsSearch(self.tree.Root))
            
    def test_seven_int(self):
        a = [3, 7, 11, 13, 17, 19, 23]
        res = [[0, 13], [1, 7], [1, 19], [2, 3], [2, 11], [2, 17], [2, 23]]
        permutations = [list(perm) for perm in itertools.permutations(a)]

        for perm in permutations:
            self.tree.GenerateTree(perm)
            self.assertEqual(self.tree.TraverseTree(), res)
            self.assertTrue(self.tree.IsBalanced(self.tree.Root))
            self.assertTrue(self.tree.IsSearch(self.tree.Root))

if __name__ == '__main__':
    print("BEFORE")
    unittest.main()
