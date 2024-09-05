import unittest
import itertools
import random

from main import HeapSort

class TestHeapSort(unittest.TestCase):
    def generate_permutations(self, n):
        a = list(range(0, n))
        return [list(perm) for perm in itertools.permutations(a)]

    def generate_shuffles(self, a, x):
        shuffles = []
        for _ in range(x):
            shuffled = a[:]
            random.shuffle(shuffled)
            shuffles.append(shuffled)
        return shuffles

    def check_heap(self, a):
        heap_sort = HeapSort(a)
        sa = sorted(a, reverse=True)
        if len(sa) != len(a):
            print("sa != a")
            return False
        #print(heap_sort.HeapObject.HeapArray)
        for i in range(0, len(sa)):
            cur_max = heap_sort.GetNextMax()
            if cur_max != sa[i]:
                print("in cycle: ", cur_max, sa[i])
                #print(heap_sort.HeapObject.HeapArray)
                return False
        return heap_sort.GetNextMax() == -1

    def test_heap_sort_0_3(self):
        a = []
        self.assertTrue(self.check_heap(a))
        a = [105]
        self.assertTrue(self.check_heap(a))
        a = [200, 100]
        self.assertTrue(self.check_heap(a))
        a = [100, 200]
        self.assertTrue(self.check_heap(a))
        a = [2, 3, 1]
        self.assertTrue(self.check_heap(a))

    def test_custom(self):
        a = [505, 404, 303, 303, 1, 1, 1, 2, 2, 3, 5, 6, 7, 10, 10, 11, 12, 105]
        shuffles = self.generate_shuffles(a, 100)
        for perm in shuffles:
            self.assertTrue(self.check_heap(perm))

    def test_heap_sort_big(self):
        for n in range(0, 10):
            print(n)
            perms = self.generate_permutations(n)
            for perm in perms:
                #print(perm)
                self.assertTrue(self.check_heap(perm))


if __name__ == '__main__':
    print("BEFORE")
    unittest.main()
