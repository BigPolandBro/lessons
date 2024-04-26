import unittest

class TestStack(unittest.TestCase):
    
    def check_ht(self, dq, size, lst):
        pass
        
    def test_hash_fun(self):
        ht = HashTable(19, 3)
        s = "abacaba"
        self.assertEqual(ht.hash_fun(s), 972445898 % 19)
        s = "aaaaaaaaa"
        self.assertEqual(ht.hash_fun(s), 550422881 % 19)
        s = "abcdefghijklmnopqrstuvwxyz"
        self.assertEqual(ht.hash_fun(s), 993009117 % 19)
    
    def test_seek_slot(self):
        ht = HashTable(19, 3)
        
        s = "ag"
        self.assertEqual(ht.seek_slot(s), 1)
        ht.slots[1] = "ag"
        
        s = "az"
        self.assertEqual(ht.seek_slot(s), 4)
        ht.slots[4] = "az"
        
        s = "bm"
        self.assertEqual(ht.seek_slot(s), 7)
        ht.slots[7] = "bm"
        
        s = "cs"
        self.assertEqual(ht.seek_slot(s), 10)
        ht.slots[10] = "cs"
        
        s = "df"
        self.assertEqual(ht.seek_slot(s), 13)
        ht.slots[13] = "df"
        
        s = "dy"
        self.assertEqual(ht.seek_slot(s), 16)
        ht.slots[16] = "dy"
        
        s = "ac"
        self.assertEqual(ht.seek_slot(s), 0)
        ht.slots[0] = "ac"
        
        s = "af"
        self.assertEqual(ht.seek_slot(s), 3)
        ht.slots[3] = "af"
        
        s = "pa"
        self.assertEqual(ht.seek_slot(s), 6)
        ht.slots[6] = "pa"
        
    def test_seek_slot_none(self):
        ht = HashTable(19, 3)
        
        st = 1
        ht.slots[st] = "marked"
        
        i = (st + ht.step) % ht.size 
        while i != st:
            ht.slots[i] = "marked"
            i = (i + ht.step) % ht.size
            
        s = "ag"
        self.assertEqual(ht.seek_slot(s), None)
    
    def test_find_none(self):
        ht = HashTable(19, 3)
        
        st = 1
        ht.slots[st] = "marked"
        
        i = (st + ht.step) % ht.size 
        while i != st:
            ht.slots[i] = "marked"
            i = (i + ht.step) % ht.size
            
        s = "ag"
        self.assertEqual(ht.find(s), None)
        
    def test_put_none(self):
        ht = HashTable(19, 3)
        
        st = 1
        ht.slots[st] = "marked"
        
        i = (st + ht.step) % ht.size 
        while i != st:
            ht.slots[i] = "marked"
            i = (i + ht.step) % ht.size
            
        s = "ag"
        self.assertEqual(ht.put(s), None)
        
    def test_find(self):
        ht = HashTable(19, 3)
        
        s = "ag"
        self.assertEqual(ht.seek_slot(s), 1)
        ht.slots[1] = "ag"
        
        s = "az"
        self.assertEqual(ht.seek_slot(s), 4)
        ht.slots[4] = "az"
        
        s = "bm"
        self.assertEqual(ht.seek_slot(s), 7)
        ht.slots[7] = "bm"
        
        s = "cs"
        self.assertEqual(ht.seek_slot(s), 10)
        ht.slots[10] = "cs"
        
        s = "df"
        self.assertEqual(ht.seek_slot(s), 13)
        ht.slots[13] = "df"
        
        s = "dy"
        self.assertEqual(ht.seek_slot(s), 16)
        ht.slots[16] = "dy"
        
        s = "ac"
        self.assertEqual(ht.seek_slot(s), 0)
        ht.slots[0] = "ac"
        
        s = "af"
        self.assertEqual(ht.seek_slot(s), 3)
        ht.slots[3] = "af"
        
        s = "pa"
        self.assertEqual(ht.seek_slot(s), 6)
        ht.slots[6] = "pa"
        
        self.assertEqual(ht.find("ag"), 1)
        self.assertEqual(ht.find("az"), 4)
        self.assertEqual(ht.find("bm"), 7)
        self.assertEqual(ht.find("cs"), 10)
        self.assertEqual(ht.find("df"), 13)
        self.assertEqual(ht.find("dy"), 16)
        self.assertEqual(ht.find("ac"), 0)
        self.assertEqual(ht.find("af"), 3)
        self.assertEqual(ht.find("pa"), 6)
        
    def test_put(self):
        ht = HashTable(19, 3)
        
        s = "ag"
        self.assertEqual(ht.put(s), 1)
        
        s = "az"
        self.assertEqual(ht.put(s), 4)
        
        s = "bm"
        self.assertEqual(ht.put(s), 7)
        
        s = "cs"
        self.assertEqual(ht.put(s), 10)
        
        s = "df"
        self.assertEqual(ht.put(s), 13)
        
        s = "dy"
        self.assertEqual(ht.put(s), 16)
        
        s = "ac"
        self.assertEqual(ht.put(s), 0)
        
        s = "af"
        self.assertEqual(ht.put(s), 3)
        
        s = "pa"
        self.assertEqual(ht.put(s), 6)
        
        self.assertEqual(ht.find("ag"), 1)
        self.assertEqual(ht.find("az"), 4)
        self.assertEqual(ht.find("bm"), 7)
        self.assertEqual(ht.find("cs"), 10)
        self.assertEqual(ht.find("df"), 13)
        self.assertEqual(ht.find("dy"), 16)
        self.assertEqual(ht.find("ac"), 0)
        self.assertEqual(ht.find("af"), 3)
        self.assertEqual(ht.find("pa"), 6)
      
if __name__ == '__main__':
    print("BEFORE")
    unittest.main()
