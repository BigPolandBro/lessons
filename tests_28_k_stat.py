import unittest
import itertools

from main import swap_elements, ArrayChunk, KthOrderStatisticsStep

def ArrayChunkLomuto(array, left, right):
    if left > right:
        return -1

    pivot_ind = (left+right)//2
    pivot = array[pivot_ind]
    array[pivot_ind], array[right] = array[right], array[pivot_ind]
    i = left - 1
    for j in range(left, right):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[right] = array[right], array[i+1]
    return i + 1

def ArrayChunkL4(M):
    iN = (len(M))//2
    i1 = 0
    i2 = len(M) - 1
    while i1 <= i2:
        while M[i1] < M[iN]:
            i1 += 1
        while M[i2] > M[iN]:
            i2 -= 1
        if i1 == i2 - 1 and M[i1] > M[i2]:
            M[i1], M[i2] = M[i2], M[i1]
            iN = ArrayChunk_(M)
            return iN
        if i1 == i2 or (i1 == i2 - 1 and M[i1] < M[i2]):
            return iN
        iN = swap_elements(M, i1, i2, iN)
    return iN

def ArrayChunk_(M):
    iN = (len(M)-1)//2
    i1 = 0
    i2 = len(M) - 1
    while i1 <= i2:
        while M[i1] < M[iN]:
            i1 += 1
        while M[i2] > M[iN]:
            i2 -= 1
        if i1 == i2 - 1 and M[i1] > M[i2]:
            M[i1], M[i2] = M[i2], M[i1]
            iN = ArrayChunk_(M)
            return iN
        if i1 == i2 or (i1 == i2 - 1 and M[i1] < M[i2]):
            return iN
        iN = swap_elements(M, i1, i2, iN)
    return iN

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

    def check_array_chunk(self, M, iN, left, right):
        if left > right:
            return True
        if len(M) == 0:
            return iN == 0
        if iN < left or iN > right:
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

    def test_array_chunk_all_perm(self):
        n = 8
        borders_list = self.generate_borders(n)
        for perm in self.generate_permutations(n):
            for borders in borders_list:
                left = borders[0]
                right = borders[1]
                M = perm[:]
                iN = ArrayChunk(M, left, right)
                if not self.check_array_chunk(M, iN, left, right):
                    print(perm, M, iN)
                self.assertTrue(self.check_array_chunk(M, iN, left, right))
                if right - left + 1 == n:
                    M2 = perm[:]
                    iN2 = ArrayChunk_(M2)
                    self.assertEqual(M, M2)
                    self.assertEqual(iN, iN2)

    def test_custom(self):
        a = [5, 6, 4, 1, 2, 3]
        newLR = KthOrderStatisticsStep(a, 0, 5, 0)
        self.assertEqual(a, [1, 2, 3, 4, 6, 5])
        self.assertTrue(self.check_array_chunk(a, 0, 0, 5))
        self.assertEqual(newLR[0], 0)
        self.assertEqual(newLR[1], 0)

        a = [5, 6, 4, 1, 2, 3]
        iN = ArrayChunkL4(a)
        self.assertEqual(a, [1, 6, 4, 5, 2, 3])
        self.assertEqual(iN, 0)

        a = [5, 6, 4, 1, 2, 3]
        iN = ArrayChunkLomuto(a, 0, 5)
        self.assertEqual(a, [3, 1, 2, 4, 5, 6])
        self.assertEqual(iN, 3)

        a = [5, 6, 4, 1, 2, 3]
        iN = ArrayChunk_(a)
        self.assertEqual(a, [1, 2, 3, 4, 6, 5])
        self.assertEqual(iN, 0)

        a = [5, 6, 7, 4, 1, 2, 3]
        newLR = KthOrderStatisticsStep(a, 0, 6, 0)
        self.assertEqual(a, [3, 2, 1, 4, 7, 6, 5])
        self.assertTrue(self.check_array_chunk(a, 3, 0, 6))
        self.assertEqual(newLR[0], 0)
        self.assertEqual(newLR[1], 2)

        a = [5, 7, 6]
        iN = ArrayChunk(a, 0, 2)
        self.assertEqual(a, [5, 6, 7])
        self.assertEqual(iN, 1)
        self.assertEqual(a[iN], 6)

        a = [5, 7, 6]
        newLR = KthOrderStatisticsStep(a, 0, 2, 0)
        self.assertEqual(a, [5, 6, 7])
        self.assertTrue(self.check_array_chunk(a, 1, 0, 2))
        self.assertEqual(newLR[0], 0)
        self.assertEqual(newLR[1], 0)

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
                    newLR = KthOrderStatisticsStep(M, left, right, k)
                    L, R = newLR[0], newLR[1]
                    self.assertTrue(L <= k <= R)
                    if SM[k - left] == M[L] and L == R:
                        iN = L
                        self.assertTrue(self.check_array_chunk(M, iN, left, right))
                    elif left == L:
                        iN = R + 1
                        self.assertTrue(SM[k - left] < M[iN])
                        self.assertTrue(self.check_array_chunk(M, iN, left, right))
                    else:
                        iN = L - 1
                        self.assertTrue(SM[k - left] > M[iN])
                        self.assertTrue(self.check_array_chunk(M, iN, left, right))


if __name__ == '__main__':
    print("BEFORE")
    unittest.main()
