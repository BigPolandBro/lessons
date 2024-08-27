import unittest
import itertools

from main import ArrayChunk, KthOrderStatisticsStep

class TestKthOrderStatisticsStep(unittest.TestCase):
    def generate_permutations(self, n):
        a = list(range(0, n))
        return [list(perm) for perm in itertools.permutations(a)]

    def generate_borders(self, n):
        borders = [[0, n - 1], [0, n // 2], [n // 2, n - 1]]
        for left in range(0, n):
            for right in range(left, n):
                borders.append([left, right])
        return borders

    def check_array_chunk(self, M, iN, left, right, pivot):
        if left > right:
            return True
        if len(M) == 0:
            return iN == 0
        if pivot != M[iN] or iN < left or iN > right:
            return False
        for i in range(left, right + 1):
            if i < iN and M[i] >= M[iN]:
                return False
            if i > iN and M[i] <= M[iN]:
                return False
        return True

    def test_k_order_stat_0_1(self):
        M = [0]
        borders = KthOrderStatisticsStep(M, 0, 0, 0)
        self.assertEqual(borders, [0, 0])
        M = []

    def test_array_chunk_all_perm(self):
        n = 8
        borders_list = self.generate_borders(n)
        for perm in self.generate_permutations(n):
            for borders in borders_list:
                left = borders[0]
                right = borders[1]
                M = perm[:]
                pivot = M[(left + right) // 2]
                iN = ArrayChunk(M, left, right)
                if not self.check_array_chunk(M, iN, left, right, pivot):
                    print(perm, M, iN, pivot)
                self.assertTrue(self.check_array_chunk(M, iN, left, right, pivot))
                if iN != -1:
                    self.assertEqual(pivot, M[iN])
                self.assertEqual(pivot, perm[(left + right) // 2])

    def test_k_order_stat(self):
        n = 8
        borders_list = self.generate_borders(n)
        for perm in self.generate_permutations(n):
            for borders in borders_list:
                left = borders[0]
                right = borders[1]
                if left > right:
                    continue
                SM = perm[left: right + 1]
                SM.sort()
                self.assertEqual(len(SM), (right - left + 1))
                for k in range(left, right):
                    M = perm[:]
                    pivot = M[(left+right)//2]
                    newLR = KthOrderStatisticsStep(M, left, right, k)
                    L, R = newLR[0], newLR[1]
                    self.assertTrue(L <= k <= R)
                    if pivot == M[L]:
                        iN = L
                        self.assertEqual(SM[k - left], M[iN])
                        self.assertEqual(L, R)
                        self.check_array_chunk(M, iN, left, right, pivot)
                    elif left == L:
                        iN = R + 1
                        self.assertTrue(SM[k - left] < M[iN])
                        self.assertEqual(pivot, M[iN])
                        self.check_array_chunk(M, iN, left, right, pivot)
                    else:
                        iN = L - 1
                        self.assertTrue(SM[k - left] > M[iN])
                        self.assertEqual(pivot, M[iN])
                        self.check_array_chunk(M, iN, left, right, pivot)


if __name__ == '__main__':
    print("BEFORE")
    unittest.main()
