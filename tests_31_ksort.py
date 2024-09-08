import unittest
import itertools
import random

from main import ksort

class Testksort_(unittest.TestCase):
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

    def generate_ok_strings(self):
        strings = []
        index = 0
        for c in "abcdefgh":
            for d1 in "0123456789":
                for d2 in "0123456789":
                    strings.append((c + d1 + d2, index))
                    index += 1
        return strings

    def test_ksort_(self):
        strings = self.generate_ok_strings()
        shuffles = self.generate_shuffles(strings, 10)
        for shuffle in shuffles:
            #print("shuffle of pairs: ", shuffle)
            ksort_ = ksort()
            self.assertEqual(ksort_.size, len(shuffle))
            self.assertEqual(len(ksort_.items), len(shuffle))
            for pair in shuffle:
                s = pair[0]
                index = pair[1]
                self.assertEqual(ksort_.index(s), index)
                self.assertTrue(ksort_.add(s))
                self.assertEqual(ksort_.items[index], s)
            # check that another adding do not break anything
            for pair in shuffle:
                s = pair[0]
                index = pair[1]
                self.assertEqual(ksort_.index(s), index)
                self.assertTrue(ksort_.add(s))
                self.assertEqual(ksort_.items[index], s)
            strings_sorted = sorted([item[0] for item in shuffle])
            self.assertEqual(ksort_.items, strings_sorted)

    def test_bad_string(self):
        bad_strings = ["aa9", "a9a", "9aa", "99a", "a9#", "9a9", "a", "aa", "aaa", "789", "78", "7", "", "A00", "A99"]
        ksort_ = ksort()
        for bad_string in bad_strings:
            #print("bad_string :", bad_string)
            self.assertEqual(ksort_.index(bad_string), -1)
            self.assertFalse(ksort_.add(bad_string))


if __name__ == '__main__':
    print("BEFORE")
    unittest.main()
