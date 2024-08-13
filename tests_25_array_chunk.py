import unittest
import itertools

class TestChunk(unittest.TestCase):
    def test_swap_elements(self):
        M = [0, 1, 2, 5, 4, 10, 15, 18]
        iN = 4
        i1 = 3
        i2 = 4
        iN = swap_elements(M, i1, i2, iN)
        self.assertEqual(iN, 3)
        self.assertEqual(M, [0, 1, 2, 4, 5, 10, 15, 18])
    
    def generate_permutations(self, n):
        a = [i for i in range(0, n)]
        return [list(perm) for perm in itertools.permutations(a)]
        
    def check_array_chunk(self, M, iN):
        if len(M) == 0:
            return iN == 0
        if iN < 0 or iN >= len(M):
            return False
        for i in range(0, len(M)):
            if i < iN and M[i] >= M[iN]:
                return False
            if i > iN and M[i] <= M[iN]:
                return False
        return True
    
    def test_array_chunk_0_1(self):
        M = []
        iN = ArrayChunk(M)
        self.assertTrue(self.check_array_chunk(M, iN))
        M = [1]
        iN = ArrayChunk(M)
        self.assertTrue(self.check_array_chunk(M, iN))
        
    def test_special(self):
        M = [0, 1, 3, 4, 5, 2]
        iN = ArrayChunk(M)
        self.assertEqual(M, [0, 1, 2, 3, 4, 5])
        self.assertEqual(iN, 3)
        # in step 4: return swap_elements(M, i1, i2, iN)
        # self.assertEqual(M, [0, 1, 3, 2, 4, 5])
        # self.assertEqual(iN, 4)
            
    def test_array_chunk_all_perm(self):
        n = 8
        for perm in self.generate_permutations(n):
            M = perm[:]
            iN = ArrayChunk(M)
            if not self.check_array_chunk(M, iN):
                print(perm, M, iN)
            self.assertTrue(self.check_array_chunk(M, iN))
        
if __name__ == '__main__':
    print("BEFORE")
    unittest.main()
