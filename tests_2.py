 import unittest

class TestLinkedList2(unittest.TestCase):
    
    def create_big_list(self):
        l_list = LinkedList2()
        node1 = Node(1)
        l_list.add_in_tail(node1)
        node2 = Node(2)
        l_list.add_in_tail(node2)
        node3 = Node(3)
        l_list.add_in_tail(node3)
        node4 = Node(2)
        l_list.add_in_tail(node4)
        self.check_l_list(l_list, 4, node1, node4, [node1, node2, node3, node4])
        return l_list
    
    def check_l_list(self, l_list : LinkedList2, size : int, head : Node, tail : Node, nodes_list):
        self.assertEqual(l_list.len(), size)
        self.assertEqual(l_list.head, head)
        self.assertEqual(l_list.tail, tail)
        self.assertEqual(l_list.get_nodes_list(), nodes_list)
        prev_node = None
        cur_node = l_list.head 
        while cur_node is not None:
            self.assertEqual(cur_node.prev, prev_node)
            prev_node = cur_node
            cur_node = cur_node.next
    
    def test_empty_list(self):
        l_list = LinkedList2()
        self.check_l_list(l_list, 0, None, None, [])
        
    def test_clean_empty_list(self):
        l_list = LinkedList2()
        l_list.clean()
        self.check_l_list(l_list, 0, None, None, [])
        
    def test_clean_big_list(self):
        l_list = self.create_big_list()
        l_list.clean()
        self.check_l_list(l_list, 0, None, None, [])
        
    def test_add_in_tail_empty_list(self):
        l_list = LinkedList2()
        new_node = Node(1)
        l_list.add_in_tail(new_node)
        self.check_l_list(l_list, 1, new_node, new_node, [new_node])

    def test_add_in_tail_big_list(self):
        l_list = LinkedList2()
        node1 = Node(1)
        l_list.add_in_tail(node1)
        node2 = Node(2)
        l_list.add_in_tail(node2)
        node3 = Node(3)
        l_list.add_in_tail(node3)
        node4 = Node(2)
        l_list.add_in_tail(node4)
        self.check_l_list(l_list, 4, node1, node4, [node1, node2, node3, node4])
        
    def test_add_in_head_empty_list(self):
        l_list = LinkedList2()
        new_node = Node(1)
        l_list.add_in_head(new_node)
        self.check_l_list(l_list, 1, new_node, new_node, [new_node])
        
    def test_add_in_head_big_list(self):
        l_list = LinkedList2()
        node1 = Node(1)
        l_list.add_in_head(node1)
        node2 = Node(2)
        l_list.add_in_head(node2)
        node3 = Node(3)
        l_list.add_in_head(node3)
        node4 = Node(2)
        l_list.add_in_head(node4)
        self.check_l_list(l_list, 4, node4, node1, [node4, node3, node2, node1])

    def test_find_in_empty_list(self):
        l_list = LinkedList2()
        found_node = l_list.find(1)
        self.assertIsNone(found_node)

    def test_find_diff_vals(self):
        l_list = LinkedList2()
        node1 = Node(1)
        l_list.add_in_tail(node1)
        node2 = Node(2)
        l_list.add_in_tail(node2)
        found_node = l_list.find(2)
        self.assertEqual(found_node, node2)
        
    def test_find_equal_vals(self):
        l_list = LinkedList2()
        node1 = Node(1)
        l_list.add_in_tail(node1)
        node2 = Node(2)
        l_list.add_in_tail(node2)
        node3 = Node(3)
        l_list.add_in_tail(node3)
        node4 = Node(2)
        l_list.add_in_tail(node4)
        found_node = l_list.find(2)
        self.assertEqual(found_node, node2)
        
    def test_find_all_empty_list(self):
        l_list = LinkedList2()
        nodes_list = l_list.find_all(1)
        self.assertEqual(nodes_list, [])
    
    def test_find_all_big_list_diff_values(self):
        l_list = LinkedList2()
        node1 = Node(1)
        l_list.add_in_tail(node1)
        node2 = Node(2)
        l_list.add_in_tail(node2)
        node3 = Node(3)
        l_list.add_in_tail(node3)
        node4 = Node(4)
        l_list.add_in_tail(node4)
        nodes_list = l_list.find_all(3)
        self.assertEqual(nodes_list, [node3])
        
    def test_find_all_big_list_equal_values(self):
        l_list = LinkedList2()
        node1 = Node(2)
        l_list.add_in_tail(node1)
        node2 = Node(2)
        l_list.add_in_tail(node2)
        node3 = Node(3)
        l_list.add_in_tail(node3)
        node4 = Node(2)
        l_list.add_in_tail(node4)
        node5 = Node(2)
        l_list.add_in_tail(node5)
        node6 = Node(4)
        l_list.add_in_tail(node6)
        node7 = Node(2)
        l_list.add_in_tail(node7)
        nodes_list = l_list.find_all(2)
        self.assertEqual(nodes_list, [node1, node2, node4, node5, node7])

    def test_delete_from_empty_list(self):
        l_list = LinkedList2()
        l_list.delete(1)
        self.check_l_list(l_list, 0, None, None, [])

    def test_delete_only_node(self):
        l_list = LinkedList2()
        node = Node(1)
        l_list.add_in_tail(node)
        l_list.delete(1)
        self.check_l_list(l_list, 0, None, None, [])
        
    def test_delete_big_list_2(self):
        l_list = LinkedList2()
        node1 = Node(2)
        l_list.add_in_tail(node1)
        node2 = Node(2)
        l_list.add_in_tail(node2)
        node3 = Node(3)
        l_list.add_in_tail(node3)
        node4 = Node(2)
        l_list.add_in_tail(node4)
        node5 = Node(2)
        l_list.add_in_tail(node5)
        node6 = Node(4)
        l_list.add_in_tail(node6)
        node7 = Node(2)
        l_list.add_in_tail(node7)
        
        l_list.delete(2)
        l_list.delete(2)
        l_list.delete(2)
        l_list.delete(2)
        l_list.delete(2)
        nodes_list = [node3, node6]
        self.check_l_list(l_list, 2, node3, node6, nodes_list)
        
    def test_delete_big_list_34(self):
        l_list = LinkedList2()
        node1 = Node(2)
        l_list.add_in_tail(node1)
        node2 = Node(2)
        l_list.add_in_tail(node2)
        node3 = Node(3)
        l_list.add_in_tail(node3)
        node4 = Node(2)
        l_list.add_in_tail(node4)
        node5 = Node(2)
        l_list.add_in_tail(node5)
        node6 = Node(4)
        l_list.add_in_tail(node6)
        node7 = Node(2)
        l_list.add_in_tail(node7)
        
        l_list.delete(3)
        l_list.delete(4)
        l_list.delete(5)
        nodes_list = l_list.find_all(2)
        self.check_l_list(l_list, 5, node1, node7, nodes_list)
        
    def test_delete_all_empty_list(self):
        l_list = LinkedList2()
        l_list.delete(1, all = True)
        l_list.delete(2, all = True)
        l_list.delete(3, all = True)
        self.check_l_list(l_list, 0, None, None, [])
        
    def test_delete_all_only_node(self):
        l_list = LinkedList2()
        node = Node(1)
        l_list.add_in_tail(node)
        l_list.delete(1, all = True)
        self.check_l_list(l_list, 0, None, None, [])
        
    def test_delete_all_big_list_2(self):
        l_list = LinkedList2()
        node1 = Node(2)
        l_list.add_in_tail(node1)
        node2 = Node(2)
        l_list.add_in_tail(node2)
        node3 = Node(3)
        l_list.add_in_tail(node3)
        node4 = Node(2)
        l_list.add_in_tail(node4)
        node5 = Node(2)
        l_list.add_in_tail(node5)
        node6 = Node(4)
        l_list.add_in_tail(node6)
        node7 = Node(2)
        l_list.add_in_tail(node7)
        
        l_list.delete(2, all = True)
        nodes_list = [node3, node6]
        self.check_l_list(l_list, 2, node3, node6, nodes_list)
        
    def test_delete_all_big_list_34(self):
        l_list = LinkedList2()
        node1 = Node(2)
        l_list.add_in_tail(node1)
        node2 = Node(2)
        l_list.add_in_tail(node2)
        node3 = Node(3)
        l_list.add_in_tail(node3)
        node4 = Node(2)
        l_list.add_in_tail(node4)
        node5 = Node(2)
        l_list.add_in_tail(node5)
        node6 = Node(4)
        l_list.add_in_tail(node6)
        node7 = Node(2)
        l_list.add_in_tail(node7)
        
        l_list.delete(3, all = True)
        l_list.delete(4, all = True)
        l_list.delete(5, all = True)
        nodes_list = l_list.find_all(2)
        self.check_l_list(l_list, 5, node1, node7, nodes_list)
        
    def test_insert_empty_list(self):
        l_list = LinkedList2()
        node = Node(1)
        l_list.insert(None, node)
        self.check_l_list(l_list, 1, node, node, [node])
    
    def test_insert_only_node_list_none(self):
        l_list = LinkedList2()
        node1 = Node(1)
        node2 = Node(2)
        l_list.insert(None, node1)
        l_list.insert(None, node2)
        self.check_l_list(l_list, 2, node1, node2, [node1, node2])
    
    def test_insert_only_node_list_not_none(self):
        l_list = LinkedList2()
        node1 = Node(1)
        node2 = Node(2)
        l_list.insert(None, node1)
        l_list.insert(node1, node2)
        self.check_l_list(l_list, 2, node1, node2, [node1, node2])
    
    def test_insert_only_node_list_middle(self):
        l_list = LinkedList2()
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        l_list.insert(None, node1)
        l_list.insert(node1, node2)
        l_list.insert(node1, node3)
        self.check_l_list(l_list, 3, node1, node2, [node1, node3, node2])
    
    def test_insert_big_list(self):
        l_list = LinkedList2()
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)
        node6 = Node(6)
        node7 = Node(7)
        l_list.insert(None, node1)
        l_list.insert(node1, node2)
        l_list.insert(node1, node3)
        l_list.insert(None, node4)
        l_list.insert(node4, node5)
        l_list.insert(node1, node6)
        l_list.insert(node6, node7)
        self.check_l_list(l_list, 7, node1, node5, [node1, node6, node7, node3, node2, node4, node5])

if __name__ == '__main__':
    print("BEFORE")
    unittest.main()

