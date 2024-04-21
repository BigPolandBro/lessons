class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None
    
    def clean(self):
        self.prev: Node = None
        self.next: Node = None

class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 == v2:
            return 0
        res = (-1 if v1 < v2 else 1)*(1 if self.__ascending else -1)
        return res

    def add(self, value):
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        
        cur = self.head 
        while cur is not None and self.compare(cur.value, value) != 1:
            cur = cur.next
            
        if cur is None:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            return
        
        if cur == self.head:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            return
        
        new_node.prev = cur.prev 
        new_node.next = cur
        cur.prev.next = new_node
        cur.prev = new_node

    def find(self, val):
        node = self.head
        while node is not None:
            if self.compare(node.value, val) == 1:
                break
            if self.compare(node.value, val) == 0:
                return node
            node = node.next
        return None

    def delete(self, val):
        cur = self.head
        while cur is not None:
            if cur.value == val:
                prv = cur.prev 
                nxt = cur.next
                if prv is not None:
                    prv.next = nxt
                    if nxt is not None:
                        nxt.prev = prv
                    else:
                        self.tail = prv
                else:
                    self.head = nxt
                    if nxt is not None:
                        nxt.prev = None
                    else:
                        self.tail = None
                break
            else:
                cur = cur.next

    def clean(self, asc):
        self.__ascending = asc
        node = self.head 
        while node is not None:
            tmp = node 
            node = node.next 
            tmp.clean() 
        self.head = None 
        self.tail = None

    def len(self):
        node = self.head 
        size = 0
        while node is not None:
            size += 1
            node = node.next
        return size

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r
        
    def get_vals(self):
        r = []
        node = self.head
        while node != None:
            r.append(node.value)
            node = node.next
        return r

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        if v1 == v2:
            return 0
        res = (-1 if v1 < v2 else 1)*(1 if self._OrderedList__ascending else -1)
        return res
