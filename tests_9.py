import unittest

class TestDict(unittest.TestCase):
    
    def check_dict(self, dq, size, lst):
        pass
        
    def test_hash_fun(self):
        ht = NativeDictionary(19)
        s = "abacaba"
        self.assertEqual(ht.hash_fun(s), 972445898 % 19)
        s = "aaaaaaaaa"
        self.assertEqual(ht.hash_fun(s), 550422881 % 19)
        s = "abcdefghijklmnopqrstuvwxyz"
        self.assertEqual(ht.hash_fun(s), 993009117 % 19)
    
    def test_is_key(self):
        ht = NativeDictionary(12)
        alp = "abcdefghijklmnopqrstuvwxyz"
        
        for i in range(0, len(alp)):
            self.assertEqual(ht.is_key(alp[i]), False)
        
        for i in range(0, ht.size):
            ht.put(alp[i], i)
        
        for i in range(0, len(alp)):
            if i < ht.size:
                self.assertEqual(ht.is_key(alp[i]), True)
            else:
                self.assertEqual(ht.is_key(alp[i]), False)
                
    def test_put(self):
        ht = NativeDictionary(12)
        alp = "abcdefghijklmnopqrstuvwxyz"
        
        for i in range(0, ht.size):
            ht.put(alp[i], i)
        
        for i in range(0, len(alp)):
            if i < ht.size:
                self.assertEqual(ht.get(alp[i]), i)
            else:
                self.assertEqual(ht.get(alp[i]), None)
                
        for i in range(0, ht.size//2):
            ht.put(alp[i], i**2)
        
        for i in range(0, len(alp)):
            if i < ht.size//2:
                self.assertEqual(ht.get(alp[i]), i**2)
            else:
                if i < ht.size:
                    self.assertEqual(ht.get(alp[i]), i)
                else:
                    self.assertEqual(ht.get(alp[i]), None)
            
    def test_get(self):
        ht = NativeDictionary(15)
        alp = "abcdefghijklmnopqrstuvwxyz"
        
        keys = ["abacaba", "aaaaaaaaa", "abcdefghijklmnopqrstuvwxyz"]
        for i in range(len(keys)):
            ht.put(keys[i], i + 100)
            
        for i in range(ht.size - len(keys)):
            ht.put(alp[i], i)
            
        for i in range(len(keys)):
            self.assertEqual(ht.get(keys[i]), i + 100)
            self.assertEqual(ht.is_key(keys[i]), True)
            
        for i in range(ht.size - len(keys)):
            self.assertEqual(ht.get(alp[i]), i)
            self.assertEqual(ht.is_key(alp[i]), True)
            
        not_keys = ["abacab", "aaaaaa", "abcdefghijklmnoqrstuvwxyz"]
        
        for key in not_keys:
            self.assertEqual(ht.get(key), None)
            self.assertEqual(ht.is_key(key), False)
            
        self.assertEqual(ht.seek_slot("lol"), None)
      
if __name__ == '__main__':
    print("BEFORE")
    unittest.main()
