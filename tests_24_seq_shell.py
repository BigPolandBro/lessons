import unittest

class TestShell(unittest.TestCase):
    def test_seq(self):
        self.assertEqual(KnuthSequence(15), [13, 4, 1])
        self.assertEqual(KnuthSequence(14), [13, 4, 1])
        self.assertEqual(KnuthSequence(13), [13, 4, 1])
        self.assertEqual(KnuthSequence(12), [4, 1])
        self.assertEqual(KnuthSequence(11), [4, 1])
        self.assertEqual(KnuthSequence(5), [4, 1])
        self.assertEqual(KnuthSequence(4), [4, 1])
        self.assertEqual(KnuthSequence(3), [1])
        self.assertEqual(KnuthSequence(1), [1])
        self.assertEqual(KnuthSequence(0), [])
        
    def test_sort(self):
        a = [1, 2, 3, 4, 5, 6, 7]
        ShellSort(a)
        self.assertEqual(a, [1, 2, 3, 4, 5, 6, 7])
        a = [7, 6, 5, 4, 3, 2, 1]
        ShellSort(a)
        self.assertEqual(a, [1, 2, 3, 4, 5, 6, 7])
        a = [7, 2, 3, 4, 5, 6, 1]
        ShellSort(a)
        self.assertEqual(a, [1, 2, 3, 4, 5, 6, 7])
        a = [7]
        ShellSort(a)
        self.assertEqual(a, [7])
        a = [2, 1, 4, 3, 6, 5, 7]
        ShellSort(a)
        self.assertEqual(a, [1, 2, 3, 4, 5, 6, 7])
        a = [3, 2, 1, 7, 6, 5, 4]
        ShellSort(a)
        self.assertEqual(a, [1, 2, 3, 4, 5, 6, 7])
        a = [3, 7, 1, 8, 4, 9, 2, 5, 6, 10]
        ShellSort(a)
        self.assertEqual(a, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        
if __name__ == '__main__':
    print("BEFORE")
    unittest.main()

