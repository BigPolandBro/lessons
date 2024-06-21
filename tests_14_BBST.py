import unittest
import itertools
import random

class TestGenerateBBSTArray(unittest.TestCase):
        
    def test_empty(self):
        a = []
        self.assertEqual(GenerateBBSTArray(a), [])
    
    def test_one(self):
        a = [404]
        self.assertEqual(GenerateBBSTArray(a), [404])
        a = ["404"]
        self.assertEqual(GenerateBBSTArray(a), ["404"])
    
    def test_three_int(self):
        a = [1, 404, 1001]
        res = [404, 1, 1001]
        permutations = [list(perm) for perm in itertools.permutations(a)]

        for perm in permutations:
            #print(perm)
            self.assertEqual(GenerateBBSTArray(perm), res)
            
    def test_three_str(self):
        a = ["alex", "azaz", "ale"]
        res = ["alex", "ale", "azaz"]
        permutations = [list(perm) for perm in itertools.permutations(a)]

        for perm in permutations:
            self.assertEqual(GenerateBBSTArray(perm), res)
            
    def test_seven_int(self):
        a = [3, 7, 11, 13, 17, 19, 23]
        res = [13, 7, 19, 3, 11, 17, 23]
        permutations = [list(perm) for perm in itertools.permutations(a)]

        for perm in permutations:
            self.assertEqual(GenerateBBSTArray(perm), res)
            
    def test_seven_str(self):
        a = ["3", "7", "11", "13", "17", "19", "23"]
        res = ["19", "13", "3", "11", "17", "23", "7"]
        permutations = [list(perm) for perm in itertools.permutations(a)]

        for perm in permutations:
            self.assertEqual(GenerateBBSTArray(perm), res)
            
    def test_fifteen_int(self):
        def generate_unique_shuffles(array, n_shuffles):
            shuffles = set()
        
            while len(shuffles) < n_shuffles:
                shuffled_array = array[:]
                random.shuffle(shuffled_array)
                shuffles.add(tuple(shuffled_array))

            unique_shuffles = [list(shuffle) for shuffle in shuffles]
            
            return unique_shuffles

        a = [i for i in range(1, 16)]
        #print(a)
        res = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
        permutations = generate_unique_shuffles(a, 10)

        for perm in permutations:
            #print(perm)
            self.assertEqual(GenerateBBSTArray(perm), res)

if __name__ == '__main__':
    print("BEFORE")
    unittest.main()

