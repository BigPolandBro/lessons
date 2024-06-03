import unittest

class TestSimpleTree(unittest.TestCase):
    
    def create_big_tree_nodes(self, nodes_list):
        root = SimpleTreeNode(0, None)
        n11 = SimpleTreeNode(11, root)
        n12 = SimpleTreeNode(12, root)
        n13 = SimpleTreeNode(13, root)
        n21 = SimpleTreeNode(11, n11)
        n22 = SimpleTreeNode(22, n11)
        n23 = SimpleTreeNode(23, n13)
        n24 = SimpleTreeNode(24, n13)
        n25 = SimpleTreeNode(25, n13)
        n31 = SimpleTreeNode(11, n21)
        n32 = SimpleTreeNode(32, n22)
        n33 = SimpleTreeNode(33, n23)
        n34 = SimpleTreeNode(34, n23)
        n35 = SimpleTreeNode(35, n23)
        n36 = SimpleTreeNode(36, n25)
        n37 = SimpleTreeNode(37, n25)
        n41 = SimpleTreeNode(11, n31)
        n42 = SimpleTreeNode(42, n37)
        n51 = SimpleTreeNode(11, n41)
        n61 = SimpleTreeNode(11, n51)
        n71 = SimpleTreeNode(11, n61)
        n81 = SimpleTreeNode(11, n71)
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
        
    def build_tree(self, root, nodes_list):
        tree = SimpleTree(root)
        for node in nodes_list:
            tree.AddChild(node.Parent, node)
        return tree
        
    def test_count(self):
        tree_nodes_list = []
        tree_nodes_dict = self.create_big_tree_nodes(tree_nodes_list)
        tree = self.build_tree(tree_nodes_dict['root'], tree_nodes_list)
        
        self.assertEqual(tree.Count(), len(tree_nodes_list))
        self.assertEqual(tree.LeafCount(), 9)
        
        subtree_nodes_list = []
        subtree_nodes_dict = self.create_subtree_nodes(subtree_nodes_list)
        subtree = self.build_tree(subtree_nodes_dict['root'], subtree_nodes_list)
        
        self.assertEqual(subtree.Count(), len(subtree_nodes_list))
        self.assertEqual(subtree.LeafCount(), 3)
        
    def test_find_nodes_small(self):
        tree_nodes_list = []
        tree_nodes_dict = self.create_subtree_nodes(tree_nodes_list)
        tree = self.build_tree(tree_nodes_dict['root'], tree_nodes_list)
        self.assertEqual(tree.FindNodesByValue(21), [tree_nodes_dict['n21']])
        
    def test_find_nodes(self):
        tree_nodes_list = []
        tree_nodes_dict = self.create_big_tree_nodes(tree_nodes_list)
        tree = self.build_tree(tree_nodes_dict['root'], tree_nodes_list)
        self.assertEqual(tree.FindNodesByValue(11), 
        [tree_nodes_dict['n11'], tree_nodes_dict['n21'], tree_nodes_dict['n31'], tree_nodes_dict['n41'], tree_nodes_dict['n51'], 
        tree_nodes_dict['n61'], tree_nodes_dict['n71'], tree_nodes_dict['n81']])
        
    def test_get_all_nodes(self):
        tree_nodes_list = []
        tree_nodes_dict = self.create_big_tree_nodes(tree_nodes_list)
        tree = self.build_tree(tree_nodes_dict['root'], tree_nodes_list)
        self.assertEqual(tree.GetAllNodes(), tree_nodes_list)
    
    def test_add_child(self):
        tree_nodes_list = []
        subtree_nodes_list = []
        
        tree_nodes_dict = self.create_big_tree_nodes(tree_nodes_list)
        subtree_nodes_dict = self.create_subtree_nodes(subtree_nodes_list)
        
        tree = self.build_tree(tree_nodes_dict['root'], tree_nodes_list)
        subtree = self.build_tree(subtree_nodes_dict['root'], subtree_nodes_list)
        
        tree.AddChild(tree_nodes_dict['n12'], subtree_nodes_dict['root'])
        
        result_nodes_list = tree_nodes_list 
        result_nodes_list[12:12] = subtree_nodes_list
        
        self.assertIn(subtree_nodes_dict['root'], tree_nodes_dict['n12'].Children)
        self.assertEqual(subtree_nodes_dict['root'].Parent, tree_nodes_dict['n12'])
        self.assertEqual(tree.GetAllNodes(), result_nodes_list)
        self.assertEqual(tree.Count(), 28)
        self.assertEqual(tree.LeafCount(), 11)
        
    def test_delete(self):
        tree_nodes_list = []
        tree_nodes_dict = self.create_big_tree_nodes(tree_nodes_list)
        tree = self.build_tree(tree_nodes_dict['root'], tree_nodes_list)

        tree.DeleteNode(tree_nodes_dict['n25'])
        result_nodes_list = tree_nodes_list[:18]
        
        self.assertNotIn(tree_nodes_dict['n25'], tree_nodes_dict['n13'].Children)
        self.assertEqual(tree_nodes_dict['n25'].Parent, None)
        self.assertEqual(tree.GetAllNodes(), result_nodes_list)
        self.assertEqual(tree.Count(), 18)
        self.assertEqual(tree.LeafCount(), 7)
        
    def test_move(self):
        tree_nodes_list = []
        tree_nodes_dict = self.create_big_tree_nodes(tree_nodes_list)
        tree = self.build_tree(tree_nodes_dict['root'], tree_nodes_list)

        tree.MoveNode(tree_nodes_dict['n25'], tree_nodes_dict['n11'])
        cut_nodes_list = tree_nodes_list[18:]
        result_nodes_list = tree_nodes_list[:18]
        result_nodes_list[11:11] = cut_nodes_list
        
        self.assertNotIn(tree_nodes_dict['n25'], tree_nodes_dict['n13'].Children)
        self.assertEqual(tree_nodes_dict['n25'].Parent, tree_nodes_dict['n11'])
        self.assertEqual(tree.GetAllNodes(), result_nodes_list)
        self.assertEqual(tree.Count(), 22)
        self.assertEqual(tree.LeafCount(), 9)
        
    def test_calc_level(self):
        tree_nodes_list = []
        tree_nodes_dict = self.create_big_tree_nodes(tree_nodes_list)
        tree = self.build_tree(tree_nodes_dict['root'], tree_nodes_list)
        
        tree.CalcLevels()
        for node_name in tree_nodes_dict.keys():
            if node_name == 'root':
                continue
            self.assertEqual(str(tree_nodes_dict[node_name].Level), node_name[1])

