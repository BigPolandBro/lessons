import unittest

class TestSimpleTree(unittest.TestCase):
    
    def create_big_tree_nodes(self, nodes_list):
        root = SimpleTreeNode(0, None)
        n11 = SimpleTreeNode(11, root)
        n12 = SimpleTreeNode(12, root)
        n13 = SimpleTreeNode(13, root)
        n21 = SimpleTreeNode(21, n11)
        n22 = SimpleTreeNode(22, n11)
        n23 = SimpleTreeNode(23, n13)
        n24 = SimpleTreeNode(24, n13)
        n25 = SimpleTreeNode(25, n13)
        n31 = SimpleTreeNode(31, n21)
        n32 = SimpleTreeNode(32, n22)
        n33 = SimpleTreeNode(33, n23)
        n34 = SimpleTreeNode(34, n23)
        n35 = SimpleTreeNode(35, n23)
        n36 = SimpleTreeNode(36, n25)
        n37 = SimpleTreeNode(37, n25)
        n41 = SimpleTreeNode(41, n31)
        n42 = SimpleTreeNode(42, n37)
        n51 = SimpleTreeNode(51, n41)
        n61 = SimpleTreeNode(61, n51)
        n71 = SimpleTreeNode(71, n61)
        n81 = SimpleTreeNode(81, n71)
        # n12 n24 n32 n33 n34 n35 n36 n42 n81
        nodes_list.extend([root, n11, n21, n31, n41, n51, n61, n71, n81, n22, n32, n12, n13, n23, n33, n34, n35, n24, n25, n36, n37, n42])
        return {
            'root': root,
            'n11': n11, 'n12': n12, 'n13': n13,
            'n21': n21, 'n22': n22, 'n23': n23, 'n24': n24, 'n25': n25,
            'n31': n31, 'n32': n32,
            'n33': n33, 'n34': n34, 'n35': n35, 'n36': n36, 'n37': n37,
            'n41': n41, 'n42': n42,
            'n51': n51,
            'n61': n61,
            'n71': n71,
            'n81': n81
        }
        
    def create_subtree_nodes(self, nodes_list):
        root = SimpleTreeNode(10, None)
        n11 = SimpleTreeNode(11, root)
        n12 = SimpleTreeNode(12, root)
        n13 = SimpleTreeNode(13, root)
        n21 = SimpleTreeNode(21, n11)
        n22 = SimpleTreeNode(23, n13)
        nodes_list.extend([root, n11, n21, n12, n13, n22])
        return {
            'root': root,
            'n11': n11, 'n12': n12, 'n13': n13,
            'n21': n21, 'n22': n22
        }
        
    def create_subtree_nodes_odd(self, nodes_list):
        root = SimpleTreeNode(10, None)
        n11 = SimpleTreeNode(11, root)
        n12 = SimpleTreeNode(12, root)
        n13 = SimpleTreeNode(13, root)
        n21 = SimpleTreeNode(21, n11)
        n22 = SimpleTreeNode(23, n13)
        n23 = SimpleTreeNode(23, n12)
        nodes_list.extend([root, n11, n21, n12, n23, n13, n22])
        return {
            'root': root,
            'n11': n11, 'n12': n12, 'n13': n13,
            'n21': n21, 'n22': n22, 'n23': n23
        }
        
    def create_subtree_nodes_two(self, nodes_list):
        root = SimpleTreeNode(10, None)
        n11 = SimpleTreeNode(11, root)
        nodes_list.extend([root, n11])
        return {
            'root': root,
            'n11': n11
        }
        
    def build_tree(self, root, nodes_list):
        tree = SimpleTree(root)
        for node in nodes_list:
            tree.AddChild(node.Parent, node)
        return tree
        
    def nodes_by_names(self, names, tree_nodes_dict):
        nodes = []
        for name in names:
            nodes.append(tree_nodes_dict[name])
        return nodes
        
    def test_even_trees(self):
        tree_nodes_list = []
        tree_nodes_dict = self.create_big_tree_nodes(tree_nodes_list)
        tree = self.build_tree(tree_nodes_dict['root'], tree_nodes_list)
        
        names = [
            'n61', 'n71', 
            'n41', 'n51', 
            'n21', 'n31', 
            'n11', 'n22', 
            'root', 'n11', 
            'n13', 'n23', 
            'n25', 'n37', 
            'n13', 'n25', 
            'root', 'n13'
            ]
        nodes = tree.EvenTrees()
        for node in nodes:
            print("| ", node.NodeValue)
        self.assertEqual(tree.EvenTrees(), self.nodes_by_names(names, tree_nodes_dict))
        
        subtree_nodes_list = []
        subtree_nodes_dict = self.create_subtree_nodes(subtree_nodes_list)
        subtree = self.build_tree(subtree_nodes_dict['root'], subtree_nodes_list)
        
        names = ['root', 'n11', 'root', 'n13']
        self.assertEqual(subtree.EvenTrees(), self.nodes_by_names(names, subtree_nodes_dict))
        
        subtree_odd_nodes_list = []
        subtree_odd_nodes_dict = self.create_subtree_nodes_odd(subtree_odd_nodes_list)
        subtree_odd = self.build_tree(subtree_odd_nodes_dict['root'], subtree_odd_nodes_list)
        
        names = []
        self.assertEqual(subtree_odd.EvenTrees(), self.nodes_by_names(names, subtree_odd_nodes_dict))
        
        subtree_two_nodes_list = []
        subtree_two_nodes_dict = self.create_subtree_nodes_two(subtree_two_nodes_list)
        subtree_two = self.build_tree(subtree_two_nodes_dict['root'], subtree_two_nodes_list)
        
        names = []
        self.assertEqual(subtree_two.EvenTrees(), self.nodes_by_names(names, subtree_two_nodes_dict))
        
        
if __name__ == '__main__':
    print("BEFORE")
    unittest.main()
