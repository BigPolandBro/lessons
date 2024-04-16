class Node:
    def __init__(self, v: int):
        self.value: int = v
        self.prev: Node = None
        self.next: Node = None
    
    def clean(self):
        self.prev: Node = None
        self.next: Node = None

class LinkedList2:  
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None

    def add_in_tail(self, item: Node) -> None:
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val: int) -> Node:
        node = self.head 
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val: int):
        node = self.head 
        res = []
        while node is not None:
            if node.value == val:
                res.append(node)
            node = node.next
        return res

    def delete(self, val: int, all: bool = False) -> None:
        prev_node = None
        cur_node = self.head
        while cur_node is not None:
            next_node = cur_node.next
            if cur_node.value == val:
                if cur_node == self.tail:
                    self.tail = prev_node
                    
                if prev_node is not None:
                    prev_node.next = next_node
                else:
                    self.head = next_node
                    
                if next_node is not None:
                        next_node.prev = prev_node
                cur_node.clean()
                
                if all == False:
                    break
            else:
                prev_node = cur_node
            cur_node = next_node

    def clean(self) -> None:
        node = self.head 
        while node is not None:
            tmp = node 
            node = node.next 
            tmp.clean() 
        self.head = None 
        self.tail = None

    def len(self) -> int:
        node = self.head 
        size = 0
        while node is not None:
            size += 1
            node = node.next
        return size

    def insert(self, afterNode: Node, newNode: Node) -> None:
        if newNode is None:
            return
        
        if afterNode is None:
            self.add_in_tail(newNode)
        else:
            newNode.next = afterNode.next
            if newNode.next is not None:
                newNode.next.prev = newNode
            else:
                self.tail = newNode
            afterNode.next = newNode
            newNode.prev = afterNode

    def add_in_head(self, newNode: Node) -> None:
        if self.head is None:
            newNode.next = None 
            self.tail = newNode
        else:
            newNode.next = self.head 
            self.head.prev = newNode
        newNode.prev = None
        self.head = newNode
        
    def get_nodes_list(self):
        nodes_list = []
        node = self.head
        while node is not None:
            nodes_list.append(node)
            node = node.next
        return nodes_list
    
    def get_vals_list(self):
        vals_list = []
        node = self.head
        while node is not None:
            vals_list.append(node.value)
            node = node.next
        return vals_list
            
class Deque:
    def __init__(self):
        self.data = LinkedList2()

    def addFront(self, item):
        node = Node(item)
        self.data.add_in_head(node)

    def addTail(self, item):
        node = Node(item)
        self.data.add_in_tail(node)

    def removeFront(self):
        if self.size() <= 0:
            return None
        cur = self.data.head
        elem = cur.value
        self.data.head = self.data.head.next 
        if self.data.head is not None:
            self.data.head.prev = None
        else:
            self.data.tail = None
        cur.clean()
        return elem
        
    def removeTail(self):
        if self.size() <= 0:
            return None
        cur = self.data.tail
        elem = cur.value
        self.data.tail = self.data.tail.prev
        if self.data.tail is not None:
            self.data.tail.next = None
        else:
            self.data.head = None
        cur.clean()
        return elem

    def size(self):
        return self.data.len()
        
def is_palindrom(str):
    order1 = Deque()
    order2 = Deque()
    for c in str:
        order1.addTail(c)
        order2.addFront(c)
    for i in range(len(str)):
        c1 = order1.removeFront()
        c2 = order2.removeFront()
        if c1 != c2:
            return False
    return True

