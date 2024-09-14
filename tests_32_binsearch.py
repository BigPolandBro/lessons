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
        a = []
        bs = BinarySearch(a)

        cnt = 0
        while bs.GetResult() == 0:
            cnt += 1
            bs.Step(404)

        self.assertEqual(cnt, 1)
        self.assertEqual(bs.Left, 0)
        self.assertEqual(bs.Right, -1)
        self.assertEqual(cnt, 1)
        self.assertEqual(bs.GetResult(), -1)

        a = [404]

        for N in [303, 404, 505]:
            bs = BinarySearch(a)
            cnt = 0
            while bs.GetResult() == 0:
                cnt += 1
                bs.Step(N)

            self.assertEqual(cnt, 1)
            if N == 404:
                self.assertEqual(bs.Left, 0)
                self.assertEqual(bs.Right, 0)
            if N > 404:
                self.assertEqual(bs.Left, 1)
                self.assertEqual(bs.Right, 0)
            if N < 404:
                self.assertEqual(bs.Left, 0)
                self.assertEqual(bs.Right, -1)
            self.assertEqual(bs.GetResult(), 1 if N in a else -1)

        a = [-404, 505]

        for N in [-404, 505, -606, 606]:
            bs = BinarySearch(a)
            cnt = 0
            while bs.GetResult() == 0:
                cnt += 1
                bs.Step(N)

            self.assertEqual(cnt, 1)
            if N == -404:
                self.assertEqual(bs.Left, 0)
                self.assertEqual(bs.Right, 1)
            if N >= 505:
                self.assertEqual(bs.Left, 1)
                self.assertEqual(bs.Right, 1)
            if N == -606:
                self.assertEqual(bs.Left, 0)
                self.assertEqual(bs.Right, -1)
            self.assertEqual(bs.GetResult(), 1 if N in a else -1)

        a = [-404, 505, 606]

        N = 505
        bs = BinarySearch(a)
        cnt = 0
        while bs.GetResult() == 0:
            cnt += 1
            bs.Step(N)

        self.assertEqual(cnt, 1)
        self.assertEqual(bs.Left, 0)
        self.assertEqual(bs.Right, 2)
        self.assertEqual(bs.GetResult(), 1)

        N = -404
        bs = BinarySearch(a)
        cnt = 0
        while bs.GetResult() == 0:
            cnt += 1
            bs.Step(N)

        self.assertEqual(cnt, 1)
        self.assertEqual(bs.Left, 0)
        self.assertEqual(bs.Right, 0)
        self.assertEqual(bs.GetResult(), 1)

        N = 606
        bs = BinarySearch(a)
        cnt = 0
        while bs.GetResult() == 0:
            cnt += 1
            bs.Step(N)

        self.assertEqual(cnt, 1)
        self.assertEqual(bs.Left, 2)
        self.assertEqual(bs.Right, 2)
        self.assertEqual(bs.GetResult(), 1)

        N = 707
        bs = BinarySearch(a)
        cnt = 0
        while bs.GetResult() == 0:
            cnt += 1
            bs.Step(N)

        self.assertEqual(cnt, 1)
        self.assertEqual(bs.Left, 2)
        self.assertEqual(bs.Right, 2)
        self.assertEqual(bs.GetResult(), -1)

    def test_fast_find(self):
        # Тестирование извлечения строки из массива найденного элемента
        array = [10, 20, 30, 40, 50, 60]
        bs = BinarySearch(array)
        cnt = 0
        while bs.GetResult() == 0:
            cnt += 1
            bs.Step(60)
        self.assertEqual(cnt, 2)
        self.assertEqual(bs.GetResult(), 1)

    def test_abundant(self):
        for n in range(0, 1000):
            a = self.generate_sorted_array(-10, 10, n)

            for N in range(-1000, 1000):
                bs = BinarySearch(a)
                while bs.GetResult() == 0:
                    # self.assertTrue(bs.Right - bs.Left > 1)
                    bs.Step(N)

                if N in a:
                    self.assertEqual(bs.GetResult(), 1)
                    if bs.Right - bs.Left > 1:
                        self.assertEqual(a[(bs.Left + bs.Right) // 2], N)
                    else:
                        self.assertTrue(a[bs.Left] == N or a[bs.Right] == N)
                else:
                    self.assertEqual(bs.GetResult(), -1)

    def test_sparse(self):
        for n in range(0, 1000):
            a = self.generate_sorted_array(-1000, 1000, n)
            #print(a)

            for N in range(-1000, 1000):
                bs = BinarySearch(a)
                while bs.GetResult() == 0:
                    # self.assertTrue(bs.Right - bs.Left > 1)
                    bs.Step(N)

                if N in a:
                    self.assertEqual(bs.GetResult(), 1)
                    if bs.Right - bs.Left > 1:
                        self.assertEqual(a[(bs.Left + bs.Right) // 2], N)
                    else:
                        self.assertTrue(a[bs.Left] == N or a[bs.Right] == N)
                else:
                    self.assertEqual(bs.GetResult(), -1)


    def test_custom(self):
        sorted_array = [1, 3, 5, 7, 9, 11, 13]

        for i in range(0, len(sorted_array)):
            N = sorted_array[i]
            binary_search = BinarySearch(sorted_array)
            while binary_search.GetResult() == 0:
                binary_search.Step(N)

            self.assertEqual(binary_search.GetResult(), 1)
            self.assertEqual((binary_search.Left + binary_search.Right) // 2, i)

        for N in [0, 2, 4, 6, 8, 10, 12, 14]:
            binary_search = BinarySearch(sorted_array)
            while binary_search.GetResult() == 0:
                binary_search.Step(N)

            self.assertEqual(binary_search.GetResult(), -1)

    def test_left_and_right_boundaries(self):
        array = [10, 20, 30, 40, 50]
        bs = BinarySearch(array)
        while bs.GetResult() == 0:
            bs.Step(10)
        self.assertEqual(bs.GetResult(), 1)

        bs = BinarySearch(array)
        while bs.GetResult() == 0:
            bs.Step(50)
        self.assertEqual(bs.GetResult(), 1)


if __name__ == '__main__':
    print("BEFORE")
    unittest.main()
