import unittest
import itertools

class TestQuickSortTailOptimization(unittest.TestCase):
    def generate_permutations(self, n):
        a = [i for i in range(0, n)]
        return [list(perm) for perm in itertools.permutations(a)]
        
    def generate_borders(self, n):
        borders = [[0, n-1], [0, n//2], [n//2, n-1]]
        for left in range(0, n):
            for right in range(0, n):
                borders.append([left, right])
        return borders
        
    def check_array_chunk(self, M, iN, left, right, pivot):
        if left > right:
            return True
        if len(M) == 0:
            return iN == 0
        if pivot != M[iN]:
            return False
        if iN < left or iN > right:
            return False
        for i in range(left, right+1):
            if i < iN and M[i] >= M[iN]:
                return False
            if i > iN and M[i] <= M[iN]:
                return False
        return True
    
    def test_array_chunk_0_1(self):
        M = []
        iN = ArrayChunk(M, 0, -1)
        self.assertTrue(self.check_array_chunk(M, iN, 0, -1, -1))
        M = [1]
        iN = ArrayChunk(M, 0, 0)
        self.assertTrue(self.check_array_chunk(M, iN, 0, 0, M[0]))
        
    def test_array_chunk_all_perm(self):
        n = 7
        borders_list = self.generate_borders(n)
        for perm in self.generate_permutations(n):
            for borders in borders_list:
                left = borders[0]
                right = borders[1]
                #print(left, right)
                M = perm[:]
                pivot = M[(left+right)//2]
                iN = ArrayChunk(M, left, right)
                if not self.check_array_chunk(M, iN, left, right, pivot):
                    print(perm, M, iN, pivot)
                self.assertTrue(self.check_array_chunk(M, iN, left, right, pivot))
                if iN != -1:
                    self.assertEqual(pivot, M[iN])
                self.assertEqual(pivot, perm[(left+right)//2])
                
    def test_k_order_stat(self):
        n = 7
        borders_list = self.generate_borders(n)
        for perm in self.generate_permutations(n):
            for borders in borders_list:
                left = borders[0]
                right = borders[1]
                if left > right: 
                    continue
                M = perm[:]
                SM = perm[left: right+1]
                SM.sort()
                self.assertEqual(len(SM), (right-left+1))
                for k in range(left, right):
                    newLR = KthOrderStatisticsStep(M, left, right, k)
                    L, R = newLR[0], newLR[1]
                    self.assertTrue(L <= k and k <= R)
                
                
        
if __name__ == '__main__':
    print("BEFORE")
    unittest.main()
