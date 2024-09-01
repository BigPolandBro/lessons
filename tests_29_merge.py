import unittest
import itertools
import random

from main import MergeSort

class TestMergeSort(unittest.TestCase):
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

    def test_merge_sort_0_3(self):
        a = []
        self.assertEqual(MergeSort(a), [])
        a = [105]
        self.assertEqual(MergeSort(a), [105])
        a = [-100, 100]
        self.assertEqual(MergeSort(a), [-100, 100])
        a = [100, -100]
        self.assertEqual(MergeSort(a), [-100, 100])
        a = [2, 3, 1]
        self.assertEqual(MergeSort(a), [1, 2, 3])

    def test_custom(self):
        a = [-505, -404, -303, -303, -1, -1, -1, 2, 2, 3, 5, 6, 7, 10, 10, 11, 12, 105]
        shuffles = self.generate_shuffles(a, 100)
        for perm in shuffles:
            self.assertEqual(MergeSort(perm), sorted(perm))
            #print(perm, MergeSort(perm), sorted(perm))

    def test_merge_sort_big(self):
        n = 9
        perms = self.generate_permutations(n)
        for perm in perms:
            start_perm = perm[:]
            python_sorted_perm = sorted(perm)
            self.assertEqual(perm, start_perm) # check that python sorted do not change input perm
            merge_sorted_perm = MergeSort(perm)
            #self.assertEqual(perm, start_perm)  # check that my MergeSort do not change input perm

            #print(perm, python_sorted_perm, merge_sorted_perm)
            self.assertEqual(python_sorted_perm, merge_sorted_perm) # check that my MergeSort result equal to correct sort
            #print(perm, python_sorted_perm, merge_sorted_perm)
            # [0, 1, 2][0, 1, 2][0, 1, 2]
            # [0, 2, 1][0, 1, 2][0, 1, 2]
            # [1, 0, 2][0, 1, 2][0, 1, 2]
            # [1, 2, 0][0, 1, 2][0, 1, 2]
            # [2, 0, 1][0, 1, 2][0, 1, 2]
            # [2, 1, 0][0, 1, 2][0, 1, 2]


if __name__ == '__main__':
    print("BEFORE")
    unittest.main()
