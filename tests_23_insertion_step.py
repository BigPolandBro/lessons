import unittest 

class TestInsertionSortStep(unittest.TestCase):
    def test_ins_sort_step1(self):
        a = [7,6,5,4,3,2,1]
        InsertionSortStep(a, 3, 0)
        self.assertEqual(a, [1,6,5,4,3,2,7])
        InsertionSortStep(a, 3, 1)
        self.assertEqual(a, [1,3,5,4,6,2,7])
        InsertionSortStep(a, 3, 2)
        self.assertEqual(a, [1,3,2,4,6,5,7])
        InsertionSortStep(a, 3, 3)
        self.assertEqual(a, [1,3,2,4,6,5,7])
    
    def test_ins_sort_step2(self):
        a = [19, 1, 8, 2, 7, 3, 6, 4, 9, 10, 15, 13, 11]
        InsertionSortStep(a, 1, 0)
        self.assertEqual(a, [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 13, 15, 19])
        
        a = [19, 1, 8, 2, 7, 3, 6, 4, 9, 10, 15, 13, 11]
        InsertionSortStep(a, 5, 0)
        self.assertEqual(a, [3, 1, 8, 2, 7, 15, 6, 4, 9, 10, 19, 13, 11])
    
    def test_ins_sort_step_empty(self):
        a = []
        InsertionSortStep(a, 5, 0)
        self.assertEqual(a, [])
        a = [10]
        InsertionSortStep(a, 1, 0)
        self.assertEqual(a, [10])
        
if __name__ == '__main__':
    print("BEFORE")
    unittest.main()
    

