import unittest
import itertools
import random

from main import BinarySearch

class TestBinarySearch(unittest.TestCase):
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

    def generate_sorted_array(self, start, end, size):
        array = [random.randint(start, end) for _ in range(size)]
        array.sort()
        return array

    def test_small(self):
        bs = BinarySearch([])

        a = []
        self.assertFalse(bs.GallopingSearch(a, 10))

        a = [404]

        for N in [303, 404, 505]:
            self.assertEqual(bs.GallopingSearch(a, N), N in a)

        a = [-404, 505]

        for N in [-404, 505, -606, 606]:
            self.assertEqual(bs.GallopingSearch(a, N), N in a)

        a = [-404, 505, 606]

        for N in [505, -404, 606, 707]:
            self.assertEqual(bs.GallopingSearch(a, N), N in a)

    def test_abundant(self):
        bs = BinarySearch([])

        for n in range(0, 1000):
            a = self.generate_sorted_array(-10, 10, n)

            for N in range(-1000, 1000):
                self.assertEqual(bs.GallopingSearch(a, N), N in a)

    def test_sparse(self):
        bs = BinarySearch([])

        for n in range(0, 1000):
            a = self.generate_sorted_array(-1000, 1000, n)
            #print(a)

            for N in range(-1000, 1000):
                self.assertEqual(bs.GallopingSearch(a, N), N in a)

    def test_custom(self):
        bs = BinarySearch([])
        a = [1, 3, 5, 7, 9, 11, 13]

        for N in a:
            self.assertTrue(bs.GallopingSearch(a, N))

        for N in [0, 2, 4, 6, 8, 10, 12, 14]:
            self.assertFalse(bs.GallopingSearch(a, N))

    def test_left_and_right_boundaries(self):
        bs = BinarySearch([])
        a = [10, 20, 30, 40, 50]
        self.assertTrue(bs.GallopingSearch(a, 10))
        self.assertTrue(bs.GallopingSearch(a, 50))


if __name__ == '__main__':
    print("BEFORE")
    unittest.main()

