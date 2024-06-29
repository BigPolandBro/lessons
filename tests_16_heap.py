import unittest
import itertools
import random

class TestHeap(unittest.TestCase):
        
    def test_make_heap(self):
        a = [1, 5, 8, 7, 6, 4, 9, 2, 3, 11]
        res = [11, 9, 4, 7, 8, 3, 1, 2, 5, 6, -1, -1, -1, -1, -1]
        
        heap = Heap()
        heap.MakeHeap(a, 3)
        self.assertEqual(heap.n, 10)
        self.assertEqual(heap.heap_size, 15)
        self.assertEqual(heap.check_heap(), True)
        self.assertEqual(set(heap.HeapArray), set(res))
        self.assertEqual(heap.GetMax(), 11)
    
    def test_empty(self):
        a = []
        res = [-1]
        heap = Heap()
        self.assertEqual(heap.n, 0)
        self.assertEqual(heap.heap_size, 0)
        self.assertEqual(heap.HeapArray, [])
        self.assertEqual(heap.GetMax(), -1)
        
        heap.MakeHeap(a, 0)
        self.assertEqual(heap.n, 0)
        self.assertEqual(heap.heap_size, 1)
        self.assertEqual(heap.HeapArray, res)
        self.assertEqual(heap.GetMax(), -1)
        
    def generate_unique_shuffles(self, array, n_shuffles):
        shuffles = set()
    
        while len(shuffles) < n_shuffles:
            shuffled_array = array[:]
            random.shuffle(shuffled_array)
            shuffles.add(tuple(shuffled_array))

        unique_shuffles = [list(shuffle) for shuffle in shuffles]
        
        return unique_shuffles
    
    def test_get_max(self):
        aa = [1001, 2, 25, 5, 10, 7, 8, 3, 9, 101, 504, 3, 205, 33, 0, 80, 678, 504, 0, 33, 3, 25, 1001]

        permutations = self.generate_unique_shuffles(aa, 10)
        
        for a in permutations:
            heap = Heap()
            heap.MakeHeap(a, 5)
            self.assertEqual(heap.check_heap(), True)
            
            b = []
            cnt = len(a)
            for i in range(len(a)):
                mx = heap.GetMax()
                b.append(mx)
                cnt -= 1
                self.assertEqual(heap.n, cnt)
                self.assertEqual(heap.check_heap(), True)
            
            self.assertEqual(heap.heap_size, 63)
            self.assertEqual(heap.n, 0)
            self.assertEqual(heap.check_heap(), True)
            
            for i in range(5):
                self.assertEqual(heap.GetMax(), -1)
            
            self.assertEqual(b, sorted(a, reverse = True))
        
    def test_add(self):
        aa = [i for i in range(31)]
        permutations = self.generate_unique_shuffles(aa, 10)
        
        for a in permutations:
            heap = Heap()
            heap.MakeHeap([], 4)
            self.assertEqual(heap.heap_size, 31)
            self.assertEqual(heap.n, 0)
            self.assertEqual(heap.check_heap(), True)

            for i in range(len(a)):
                self.assertEqual(heap.Add(a[i]), True)
                self.assertEqual(heap.check_heap(), True)
            
            self.assertEqual(heap.heap_size, 31)
            self.assertEqual(heap.n, 31)
            
            self.assertEqual(heap.Add(100), False)
            
            b = []
            cnt = heap.n
            for i in range(heap.n):
                b.append(heap.GetMax())
                cnt -= 1
                self.assertEqual(heap.n, cnt)
                self.assertEqual(heap.check_heap(), True)
                
            self.assertEqual(b, sorted(a, reverse = True))

if __name__ == '__main__':
    print("BEFORE")
    unittest.main()    	
