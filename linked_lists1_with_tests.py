class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        node = self.head
        result = []
        while node is not None:
            if node.value == val:
                result.append(node)
            node = node.next
        return result

    def delete(self, val, all=False):
        prev_node = None
        cur_node = self.head
        while cur_node is not None:
            next_node = cur_node.next
            if cur_node.value == val:
                if cur_node == self.tail:
                    self.tail = prev_node
                cur_node.next = None
                if prev_node is None:
                    self.head = next_node
                else:
                    prev_node.next = next_node
                if all == False:
                    break
            else:
                prev_node = cur_node
            cur_node = next_node
        pass

    def clean(self):
        node = self.head
        while node is not None:
            tmp = node
            node = node.next
            tmp.next = None
        self.head = None
        self.tail = None
        pass

    def len(self):
        size = 0
        node = self.head
        while node is not None:
            size += 1
            node = node.next
        return size

    def insert(self, afterNode, newNode):
        if afterNode is None:
            newNode.next = self.head
            self.head = newNode
        else:
            newNode.next = afterNode.next
            afterNode.next = newNode
        if afterNode == self.tail:
            self.tail = newNode
        pass
    
    def check(self, size, head, tail, nodes_list):
        assert self.len() == size
        assert self.head == head 
        assert self.tail == tail 
        self_nodes_list = []
        node = self.head
        while node is not None:
            self_nodes_list.append(node)
            node = node.next
        assert self_nodes_list == nodes_list
        
def sum_linked_lists(l1, l2):
    res = []
    if l1.len() == l2.len():
        node1 = l1.head
        node2 = l2.head
        while node1 is not None and node2 is not None:
            res.append(node1.value + node2.value)
            node1 = node1.next
            node2 = node2.next 
    return res

def check_empty():
    print("check_empty")
    node11 = Node(1)
    node12 = Node(1)
    node13 = Node(1)
    
    node21 = Node(2)
    node22 = Node(2)
    node23 = Node(2)
    
    node31 = Node(3)
    node32 = Node(3)
    node33 = Node(3)
    
    node41 = Node(4)
    
    l = LinkedList()
    l.check(0, None, None, [])
    
    l.delete(1)
    l.check(0, None, None, []) 
    
    l.delete(2, True)
    l.check(0, None, None, [])
    
    l.clean()
    l.check(0, None, None, [])
    
    res = l.find_all(3)
    assert(res == [])
    l.check(0, None, None, [])
    
    l.insert(l.head, node11)
    l.check(1, node11, node11, [node11])
    
def check_1():
    print("check_1")
    node11 = Node(1)
    node12 = Node(1)
    node13 = Node(1)
    
    node21 = Node(2)
    node22 = Node(2)
    node23 = Node(2)
    
    node31 = Node(3)
    node32 = Node(3)
    node33 = Node(3)
    
    node41 = Node(4)
    
    l = LinkedList()
    l.add_in_tail(node11)
    l.check(1, node11, node11, [node11])
    
    l.delete(2)
    l.check(1, node11, node11, [node11])
    
    l.delete(2, True)
    l.check(1, node11, node11, [node11])
    
    l.delete(1)
    l.check(0, None, None, [])
    
    l = LinkedList()
    l.add_in_tail(node11)
    
    l.delete(1, True)
    l.check(0, None, None, [])
    
    l = LinkedList()
    l.add_in_tail(node11)
    
    l.clean()
    l.check(0, None, None, [])
    
    l = LinkedList()
    l.add_in_tail(node11)
    
    res = l.find_all(3)
    assert(res == [])
    l.check(1, node11, node11, [node11])
    
    res = l.find_all(1)
    assert(res == [node11])
    l.check(1, node11, node11, [node11])
    
    l.insert(None, node21)
    l.check(2, node21, node11, [node21, node11])
    
    l.insert(l.tail, node31)
    l.check(3, node21, node31, [node21, node11, node31])
    
    l.insert(node11, node41)
    l.check(4, node21, node31, [node21, node11, node41, node31])
    
def check_2_diff():
    print("check_2_diff")
    node11 = Node(1)
    node12 = Node(1)
    node13 = Node(1)
    
    node21 = Node(2)
    node22 = Node(2)
    node23 = Node(2)
    
    node31 = Node(3)
    node32 = Node(3)
    node33 = Node(3)
    
    node41 = Node(4)
    
    l = LinkedList()
    l.add_in_tail(node11)
    l.add_in_tail(node31)
    l.check(2, node11, node31, [node11, node31])
    
    l.delete(2)
    l.check(2, node11, node31, [node11, node31])
    
    l.delete(2, True)
    l.check(2, node11, node31, [node11, node31])
    
    l.delete(1)
    l.check(1, node31, node31, [node31])
    
    l.delete(3, True)
    l.check(0, None, None, [])
    
    l = LinkedList()
    l.add_in_tail(node11)
    l.add_in_tail(node31)
    l.check(2, node11, node31, [node11, node31])
    
    l.clean()
    l.check(0, None, None, [])
    
    l.add_in_tail(node11)
    l.add_in_tail(node31)
    l.check(2, node11, node31, [node11, node31])
    
    res = l.find_all(2)
    assert(res == [])
    l.check(2, node11, node31, [node11, node31])
    
    res = l.find_all(1)
    assert(res == [node11])
    l.check(2, node11, node31, [node11, node31])
    
    res = l.find_all(3)
    assert(res == [node31])
    l.check(2, node11, node31, [node11, node31])
    
    l.insert(None, node21)
    l.check(3, node21, node31, [node21, node11, node31])
    
    l.insert(node21, node22)
    l.check(4, node21, node31, [node21, node22, node11, node31])
    
def check_2_equal():
    print("check_2_equal")
    node11 = Node(1)
    node12 = Node(1)
    node13 = Node(1)
    
    node21 = Node(2)
    node22 = Node(2)
    node23 = Node(2)
    
    node31 = Node(3)
    node32 = Node(3)
    node33 = Node(3)
    
    node41 = Node(4)
    
    l = LinkedList()
    l.add_in_tail(node11)
    l.add_in_tail(node12)
    l.check(2, node11, node12, [node11, node12])
    
    res = l.find_all(1)
    assert res == [node11, node12]
    l.check(2, node11, node12, [node11, node12])
    
    l.delete(1)
    l.check(1, node12, node12, [node12])
    
    l.insert(None, node11)
    l.check(2, node11, node12, [node11, node12])
    
    l.delete(1, True)
    l.check(0, None, None, [])
    
def check_multi():
    print("check_multi")
    node11 = Node(1)
    node12 = Node(1)
    node13 = Node(1)
    
    node21 = Node(2)
    node22 = Node(2)
    node23 = Node(2)
    
    node31 = Node(3)
    node32 = Node(3)
    node33 = Node(3)
    
    node41 = Node(4)
    
    l = LinkedList()
    l.add_in_tail(node11)
    l.add_in_tail(node12)
    l.add_in_tail(node21)
    l.add_in_tail(node31)
    l.add_in_tail(node32)
    l.add_in_tail(node33)
    l.add_in_tail(node41)
    l.check(7, node11, node41, [node11, node12, node21, node31, node32, node33, node41])
    
    res = l.find_all(1)
    assert res == [node11, node12]
    l.check(7, node11, node41, [node11, node12, node21, node31, node32, node33, node41])
    
    res = l.find_all(2)
    assert res == [node21]
    l.check(7, node11, node41, [node11, node12, node21, node31, node32, node33, node41])
    
    res = l.find_all(3)
    assert res == [node31, node32, node33]
    l.check(7, node11, node41, [node11, node12, node21, node31, node32, node33, node41])
    
    res = l.find_all(4)
    assert res == [node41]
    l.check(7, node11, node41, [node11, node12, node21, node31, node32, node33, node41])
    
    l.delete(2, True)
    l.check(6, node11, node41, [node11, node12, node31, node32, node33, node41])
    
    l.delete(1, True)
    l.check(4, node31, node41, [node31, node32, node33, node41])
    
    l.insert(None, node21)
    l.delete(3, True)
    l.check(2, node21, node41, [node21, node41])
    
    l.insert(node21, node22)
    l.check(3, node21, node41, [node21, node22, node41])
    
    l.clean()
    l.check(0, None, None, [])
    
def check_sum():
    print("check_sum")
    node11 = Node(1)
    node12 = Node(1)
    node13 = Node(1)
    
    node21 = Node(2)
    node22 = Node(2)
    node23 = Node(2)
    
    node31 = Node(3)
    node32 = Node(3)
    node33 = Node(3)
    
    node41 = Node(4)
    
    l1 = LinkedList()
    l1.add_in_tail(node11)
    l1.add_in_tail(node21)
    l1.add_in_tail(node31)
    
    l2 = LinkedList()
    l2.add_in_tail(node22)
    l2.add_in_tail(node32)
    l2.add_in_tail(node33)
    
    l1.check(3, node11, node31, [node11, node21, node31])
    l2.check(3, node22, node33, [node22, node32, node33])
    
    assert sum_linked_lists(l1, l2) == [3, 5, 6]


