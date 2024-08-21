import unittest
import itertools

class TestChunk(unittest.TestCase):
        
    def test_special(self):
        M = [0, 1, 3, 4, 5, 2]
        iN = ArrayChunk(M)
        self.assertEqual(M, [0, 1, 3, 2, 4, 5])
        self.assertEqual(iN, 4)
        
    def test_special2(self):
        M = [6, 5, 7]
        iN = ArrayChunk(M)
        self.assertEqual(M, [5, 6, 7])
        self.assertEqual(iN, 0)
        
if __name__ == '__main__':
    print("BEFORE")
    unittest.main()


