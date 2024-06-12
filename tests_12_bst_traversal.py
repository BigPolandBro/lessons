import unittest

class TestBSTTraversalMethods(unittest.TestCase):

    def setUp(self):
        # Tree:
        #
        #         10
        #        /   \
        #       5     15
        #      / \    / \
        #     3   8  12  18
        #        /  /  \
        #       7  11  13
        self.root = BSTNode(10, "Root", None)
        self.tree = BST(self.root)
        self.tree.AddKeyValue(5, "Left")
        self.tree.AddKeyValue(15, "Right")
        self.tree.AddKeyValue(3, "LeftLeft")
        self.tree.AddKeyValue(8, "LeftRight")
        self.tree.AddKeyValue(7, "LeftRightLeft")
        self.tree.AddKeyValue(12, "RightLeft")
        self.tree.AddKeyValue(13, "RightLeftRight")
        self.tree.AddKeyValue(11, "RightLeftLeft")
        self.tree.AddKeyValue(18, "RightRight")

    def test_wide_all_nodes(self):
        nodes = self.tree.WideAllNodes()
        keys = [node.NodeKey for node in nodes]
        expected_keys = [10, 5, 15, 3, 8, 12, 18, 7, 11, 13]
        self.assertEqual(keys, expected_keys)

    def test_deep_all_nodes_in_order(self):
        nodes = self.tree.DeepAllNodes(0)
        keys = [node.NodeKey for node in nodes]
        expected_keys = [3, 5, 7, 8, 10, 11, 12, 13, 15, 18]
        self.assertEqual(keys, expected_keys)

    def test_deep_all_nodes_post_order(self):
        nodes = self.tree.DeepAllNodes(1)
        keys = [node.NodeKey for node in nodes]
        expected_keys = [3, 7, 8, 5, 11, 13, 12, 18, 15, 10]
        self.assertEqual(keys, expected_keys)

    def test_deep_all_nodes_pre_order(self):
        nodes = self.tree.DeepAllNodes(2)
        keys = [node.NodeKey for node in nodes]
        expected_keys = [10, 5, 3, 8, 7, 15, 12, 11, 13, 18]
        self.assertEqual(keys, expected_keys)
        
    def test_invert(self):
        self.tree.InvertTree()
        nodes = self.tree.DeepAllNodes(0)
        keys = [node.NodeKey for node in nodes]
        expected_keys = [18, 15, 13, 12, 11, 10, 8, 7, 5, 3]
        self.assertEqual(keys, expected_keys)
        
        nodes = self.tree.DeepAllNodes(1)
        keys = [node.NodeKey for node in nodes]
        expected_keys = [18, 13, 11, 12, 15, 7, 8, 3, 5, 10]
        self.assertEqual(keys, expected_keys)
        
        nodes = self.tree.DeepAllNodes(2)
        keys = [node.NodeKey for node in nodes]
        expected_keys = [10, 15, 18, 12, 13, 11, 5, 8, 7, 3]
        self.assertEqual(keys, expected_keys)

if __name__ == '__main__':
    print("BEFORE")
    unittest.main()
            
          
