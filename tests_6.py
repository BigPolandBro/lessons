import unittest

class TestStack(unittest.TestCase):
    
    def check_deque(self, dq, size, lst):
        self.assertEqual(size, dq.size())
        self.assertEqual(dq.data.get_vals_list(), lst)
    
    def test_add_front(self):
        dq = Deque()
        self.check_deque(dq, 0, [])
        dq.addFront(1)
        self.check_deque(dq, 1, [1])
        dq.addFront(2)
        self.check_deque(dq, 2, [2, 1])
        dq.addFront(3)
        self.check_deque(dq, 3, [3, 2, 1])
    
    def test_add_tail(self):
        dq = Deque()
        self.check_deque(dq, 0, [])
        dq.addTail(1)
        self.check_deque(dq, 1, [1])
        dq.addTail(2)
        self.check_deque(dq, 2, [1, 2])
        dq.addTail(3)
        self.check_deque(dq, 3, [1, 2, 3])
        
    def test_add_front(self):
        dq = Deque()
        dq.addFront(1)
        dq.addFront(2)
        dq.addFront(3)
        self.check_deque(dq, 3, [3, 2, 1])
        a = dq.removeFront()
        self.check_deque(dq, 2, [2, 1])
        b = dq.removeFront()
        self.check_deque(dq, 1, [1])
        c = dq.removeFront()
        self.check_deque(dq, 0, [])
        
        self.assertEqual(a, 3)
        self.assertEqual(b, 2)
        self.assertEqual(c, 1)
    
    def test_remove_tail(self):
        dq = Deque()
        dq.addTail(1)
        dq.addTail(2)
        dq.addTail(3)
        self.check_deque(dq, 3, [1, 2, 3])
        a = dq.removeTail()
        self.check_deque(dq, 2, [1, 2])
        b = dq.removeTail()
        self.check_deque(dq, 1, [1])
        c = dq.removeTail()
        self.check_deque(dq, 0, [])
        
        self.assertEqual(a, 3)
        self.assertEqual(b, 2)
        self.assertEqual(c, 1)

    def test_is_palindrom(self):
        self.assertEqual(is_palindrom("kazak"), True)
        self.assertEqual(is_palindrom("kazan"), False)
        self.assertEqual(is_palindrom("abacaba"), True)
        self.assertEqual(is_palindrom("abba"), True)
        self.assertEqual(is_palindrom("aa"), True)
        self.assertEqual(is_palindrom("a"), True)
        self.assertEqual(is_palindrom("abacaca"), False)
        
if __name__ == '__main__':
    print("BEFORE")
    unittest.main()
