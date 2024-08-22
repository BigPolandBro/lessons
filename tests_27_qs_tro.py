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
        
    def check_array_chunk(self, M, iN, left, right):
        if left > right:
            return True
        if len(M) == 0:
            return iN == 0
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
        self.assertTrue(self.check_array_chunk(M, iN, 0, -1))
        M = [1]
        iN = ArrayChunk(M, 0, 0)
        self.assertTrue(self.check_array_chunk(M, iN, 0, 0))
        
    # def test_array_chunk_all_perm(self):
    #     n = 8
    #     borders_list = self.generate_borders(n)
    #     for perm in self.generate_permutations(n):
    #         for borders in borders_list:
    #             left = borders[0]
    #             right = borders[1]
    #             #print(left, right)
    #             M = perm[:]
    #             iN = ArrayChunk(M, left, right)
    #             if not self.check_array_chunk(M, iN, left, right):
    #                 print(perm, M, iN)
    #             self.assertTrue(self.check_array_chunk(M, iN, left, right))
        
    def check_sorted(self, M, left, right):
        for i in range(left + 1, right + 1):
            #print(M[i-1], M[i])
            if M[i-1] >= M[i]:
                return False
        return True
        
    def test_custom(self):
        perm = [0, 1, 2, 3, 5, 4]
        M = [0, 1, 2, 3, 5, 4]
        left = 0 
        right = 5
        QuickSortTailOptimization(M, left, right)
        if not self.check_sorted(M, left, right):
            print(perm, M, left, right)
        self.assertTrue(self.check_sorted(M, left, right))
        perm = [5, 4, 404, 3, 11, 0, 1, 2, 10, 505, 110, 202, 118]
        M = perm[:]
        left = 0 
        right = 12
        QuickSortTailOptimization(M, left, right)
        print(M, perm)
        if not self.check_sorted(M, left, right):
            print(perm, M, left, right)
        self.assertTrue(self.check_sorted(M, left, right))
        SM = sorted(M)
        self.assertEqual(M, SM)
        self.assertEqual(M, [0, 1, 2, 3, 4, 5, 10, 11, 110, 118, 202, 404, 505])
        
    def test_quick_sort_all_perm(self):
        n = 7
        borders_list = self.generate_borders(n)
        for perm in self.generate_permutations(n):
            for borders in borders_list:
                left = borders[0]
                right = borders[1]
                M = perm[:]
                QuickSortTailOptimization(M, left, right)
                if not self.check_sorted(M, left, right):
                    print(perm, M, left, right)
                self.assertTrue(self.check_sorted(M, left, right))
        
if __name__ == '__main__':
    print("BEFORE")
    unittest.main()
