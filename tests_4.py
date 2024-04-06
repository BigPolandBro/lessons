import unittest

class TestStack(unittest.TestCase):
    
    def check_stack(self, st, size, lst):
        self.assertEqual(size, st.size())
        self.assertEqual(st.stack, lst)
    
    def test_pop(self):
        st = Stack()
        self.check_stack(st, 0, [])
        self.assertEqual(st.pop(), None)
        st.push(5)
        st.push(1)
        self.check_stack(st, 2, [5, 1])
        self.assertEqual(st.pop(), 1)
        self.check_stack(st, 1, [5])
        self.assertEqual(st.pop(), 5)
        self.check_stack(st, 0, [])
        self.assertEqual(st.pop(), None)
        
    def test_push(self):
        st = Stack()
        self.check_stack(st, 0, [])
        st.push(1)
        st.push(1)
        st.push(2)
        st.push(3)
        st.push(3)
        self.check_stack(st, 5, [1, 1, 2, 3, 3])
        
    def test_peek(self):
        st = Stack()
        self.check_stack(st, 0, [])
        self.assertEqual(st.peek(), None)
        st.push(5)
        st.push(1)
        self.check_stack(st, 2, [5, 1])
        self.assertEqual(st.peek(), 1)
        self.check_stack(st, 2, [5, 1])
        self.assertEqual(st.peek(), 1)
        st.pop()
        self.check_stack(st, 1, [5])
        self.assertEqual(st.peek(), 5)
        st.pop()
        self.check_stack(st, 0, [])
        self.assertEqual(st.peek(), None)
        
    def test_check_balanced(self):
        self.assertEqual(check_balanced(""), True)
        self.assertEqual(check_balanced("()"), True)
        self.assertEqual(check_balanced("("), False)
        self.assertEqual(check_balanced(")"), False)
        self.assertEqual(check_balanced(")("), False)
        self.assertEqual(check_balanced("())("), False)
        self.assertEqual(check_balanced("))(("), False)
        self.assertEqual(check_balanced("((())"), False)
        self.assertEqual(check_balanced("(()((())()))"), True)
        self.assertEqual(check_balanced("(()()(()"), False)
        
if __name__ == '__main__':
    print("BEFORE")
    unittest.main()

