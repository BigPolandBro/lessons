import unittest

class Test_aBST(unittest.TestCase):

    def setUp(self):
        # Tree:
        #
        #     (0) 10
        #        /   \
        #       5     15
        #      / \      \
        #     3   8     18
        self.tree = aBST(2)
        
    def test_tree_size(self):
        self.assertEqual(len(self.tree.Tree), 7)
    
    def test_one_node_tree(self):
        tree = aBST(0)
        self.assertEqual(len(tree.Tree), 1)
        self.assertEqual(tree.FindKeyIndex(10), 0)
        self.assertEqual(tree.AddKey(10), 0)
        self.assertEqual(tree.FindKeyIndex(10), 0)
        self.assertEqual(tree.FindKeyIndex(11), None)
        self.assertEqual(tree.AddKey(11), -1)

    def test_find_key_index(self):
        # test +0 and -0
        self.assertEqual(self.tree.FindKeyIndex(10), 0)
        index = self.tree.AddKey(10)
        self.assertEqual(index, 0)
        self.assertEqual(self.tree.Tree[index], 10)
        self.assertEqual(self.tree.FindKeyIndex(10), 0)
        
        # test +ind -ind
        self.assertEqual(self.tree.FindKeyIndex(5), -1)
        index = self.tree.AddKey(5)
        self.assertEqual(index, 1)
        self.assertEqual(self.tree.Tree[index], 5)
        self.assertEqual(self.tree.FindKeyIndex(5), 1)
        
        # test +ind -ind
        self.assertEqual(self.tree.FindKeyIndex(8), -4)
        index = self.tree.AddKey(8)
        self.assertEqual(index, 4)
        self.assertEqual(self.tree.Tree[index], 8)
        self.assertEqual(self.tree.FindKeyIndex(8), 4)
        
        #test None
        self.assertEqual(self.tree.FindKeyIndex(6), None)
        self.assertEqual(self.tree.FindKeyIndex(7), None)
        self.assertEqual(self.tree.FindKeyIndex(9), None)
        
        self.assertEqual(self.tree.FindKeyIndex(3), -3)
        index = self.tree.AddKey(3)
        self.assertEqual(index, 3)
        self.assertEqual(self.tree.Tree[index], 3)
        self.assertEqual(self.tree.FindKeyIndex(3), 3)
        
        #test None
        self.assertEqual(self.tree.FindKeyIndex(1), None)
        self.assertEqual(self.tree.FindKeyIndex(2), None)
        self.assertEqual(self.tree.FindKeyIndex(4), None)

    def test_add_key(self):
        self.assertEqual(self.tree.Tree[0], None)
        index = self.tree.AddKey(10)
        self.assertEqual(index, 0)
        
        self.assertEqual(self.tree.Tree[1], None)
        index = self.tree.AddKey(5)
        self.assertEqual(index, 1)

        self.assertEqual(self.tree.Tree[4], None)
        index = self.tree.AddKey(8)
        self.assertEqual(index, 4)
        self.assertEqual(self.tree.Tree[index], 8)
        
        #test -1
        self.assertEqual(self.tree.AddKey(6), -1)
        self.assertEqual(self.tree.AddKey(7), -1)
        self.assertEqual(self.tree.AddKey(9), -1)
        
        self.assertEqual(self.tree.Tree[3], None)
        index = self.tree.AddKey(3)
        self.assertEqual(index, 3)
        self.assertEqual(self.tree.Tree[index], 3)
        
        #test -1
        self.assertEqual(self.tree.AddKey(1), -1)
        self.assertEqual(self.tree.AddKey(2), -1)
        self.assertEqual(self.tree.AddKey(4), -1)
        
        self.assertEqual(self.tree.Tree[2], None)
        index = self.tree.AddKey(15)
        self.assertEqual(index, 2)
        
        self.assertEqual(self.tree.Tree[6], None)
        index = self.tree.AddKey(18)
        self.assertEqual(index, 6)
        
        self.assertEqual(self.tree.Tree[5], None)
        index = self.tree.AddKey(12)
        self.assertEqual(index, 5)
        
        #test -1
        self.assertEqual(self.tree.AddKey(13), -1)
        self.assertEqual(self.tree.AddKey(14), -1)
        self.assertEqual(self.tree.AddKey(16), -1)
        self.assertEqual(self.tree.AddKey(17), -1)
        self.assertEqual(self.tree.AddKey(20), -1)
        self.assertEqual(self.tree.AddKey(100), -1)
        self.assertEqual(self.tree.AddKey(-100), -1)
        
        self.assertEqual(self.tree.Tree[0], 10)
        self.assertEqual(self.tree.Tree[1], 5)
        self.assertEqual(self.tree.Tree[2], 15)
        self.assertEqual(self.tree.Tree[3], 3)
        self.assertEqual(self.tree.Tree[4], 8)
        self.assertEqual(self.tree.Tree[5], 12)
        self.assertEqual(self.tree.Tree[6], 18)

if __name__ == '__main__':
    print("BEFORE")
    unittest.main()

