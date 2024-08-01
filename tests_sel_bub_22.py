import unittest

class TestSort(unittest.TestCase):
    def test_selection(self):
        a = []
        SelectionSortStep(a, 0)
        self.assertEqual(a, [])
        a = [1]
        SelectionSortStep(a, 0)
        self.assertEqual(a, [1])
        a = [1, 2]
        SelectionSortStep(a, 1)
        self.assertEqual(a, [1, 2])
        SelectionSortStep(a, 0)
        self.assertEqual(a, [1, 2])
        a = [3, 7, 4, 5, 2]
        SelectionSortStep(a, 0)
        self.assertEqual(a, [2, 7, 4, 5, 3])
        a = [3, 7, 4, 5, 2]
        SelectionSortStep(a, 2)
        self.assertEqual(a, [3, 7, 2, 5, 4])
        a = [3, 1, 4, 5, 2]
        SelectionSortStep(a, 1)
        self.assertEqual(a, [3, 1, 4, 5, 2])
        a = [3, 4, 1, 5, 2]
        SelectionSortStep(a, 1)
        self.assertEqual(a, [3, 1, 4, 5, 2])
        a = [3, 4, 1, 5, 2]
        SelectionSortStep(a, 5)
        self.assertEqual(a, [3, 4, 1, 5, 2])
        a = [3, 4, 1, 5, 2]
        SelectionSortStep(a, 15)
        self.assertEqual(a, [3, 4, 1, 5, 2])
        
    def test_bubble(self):
        a = []
        self.assertEqual(BubbleSortStep(a), True)
        self.assertEqual(a, [])
        a = [1]
        self.assertEqual(BubbleSortStep(a), True)
        self.assertEqual(a, [1])
        a = [1, 2]
        self.assertEqual(BubbleSortStep(a), True)
        self.assertEqual(a, [1, 2])
        a = [3, 7, 4, 5, 2]
        self.assertEqual(BubbleSortStep(a), False)
        self.assertEqual(a, [3, 4, 5, 2, 7])
        a = [1, 2, 3, 4, 5]
        self.assertEqual(BubbleSortStep(a), True)
        self.assertEqual(a, [1, 2, 3, 4, 5])
        a = [1, 1, 2, 2, 2, 4, 4]
        self.assertEqual(BubbleSortStep(a), True)
        self.assertEqual(a, [1, 1, 2, 2, 2, 4, 4])
        a = [5, 4, 3, 2, 1]
        self.assertEqual(BubbleSortStep(a), False)
        self.assertEqual(a, [4, 3, 2, 1, 5])
        a = [2, 1, 3, 4, 5]
        self.assertEqual(BubbleSortStep(a), False)
        self.assertEqual(a, [1, 2, 3, 4, 5])
        a = [1, 2, 4, 3, 5]
        self.assertEqual(BubbleSortStep(a), False)
        self.assertEqual(a, [1, 2, 3, 4, 5])
        a = [1, 2, 3, 5, 4]
        self.assertEqual(BubbleSortStep(a), False)
        self.assertEqual(a, [1, 2, 3, 4, 5])
        a = [4, 3, 1, 2]
        self.assertEqual(BubbleSortStep(a), False)
        self.assertEqual(a, [3, 1, 2, 4])
        
if __name__ == '__main__':
    print("BEFORE")
    unittest.main()
