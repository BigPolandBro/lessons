import unittest

class TestStack(unittest.TestCase):
    
    def check_queue(self, q, size, lst):
        self.assertEqual(size, st.size())
        self.assertEqual(st.stack, lst)
    
    def test_queue(self):
        q = Queue()
        self.assertEqual(q.dequeue(), None)
        q.enqueue(5)
        q.enqueue(1)
        self.assertEqual(q.size(), 2)
        self.assertEqual(q.dequeue(), 5)
        self.assertEqual(q.size(), 1)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.size(), 0)
        self.assertEqual(q.dequeue(), None)
        q.enqueue(100)
        self.assertEqual(q.size(), 1)
        self.assertEqual(q.dequeue(), 100)
        self.assertEqual(q.size(), 0)
        self.assertEqual(q.dequeue(), None)
        
    def test_rotate(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        q.enqueue(5)
        q.enqueue(6)
        q.enqueue(7)
        q.rotate(4)
        cmp = [5, 6, 7, 1, 2, 3, 4]
        check = []
        while q.size() > 0:
            check.append(q.dequeue())
        self.assertEqual(check, cmp)
        
if __name__ == '__main__':
    print("BEFORE")
    unittest.main()
