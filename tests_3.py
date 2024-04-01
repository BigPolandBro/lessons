import unittest

class TestDynArray(unittest.TestCase):
    
    def check_array(self, arr, capacity, count, lst):
        self.assertEqual(capacity, arr.capacity)
        self.assertEqual(count, arr.count)
        for i in range(0, count):
            self.assertEqual(arr.array[i], lst[i])
    
    def test_insert_capacity_ok(self):
        arr = DynArray()
        lst = [3, 4, 1, 5, 2, 6]
        arr.append(1)
        arr.insert(1, 2)
        arr.insert(0, 3)
        arr.insert(1, 4)
        arr.insert(3, 5)
        arr.insert(5, 6)
        self.check_array(arr, 16, 6, lst)
        
    def test_insert_capacity_rise(self):
        arr = DynArray()
        lst = []
        for i in range(0, 16):
            lst.append(i+1)
            arr.insert(arr.count, i+1)
        arr.insert(5, 404)
        lst.insert(5, 404)
        self.check_array(arr, 32, 17, lst)
        
    def test_insert_error(self):
        arr = DynArray()
        with self.assertRaises(IndexError):
            arr.insert(1, 1)
        lst = [3, 4, 1, 5, 2, 6]
        arr.append(1)
        arr.insert(1, 2)
        arr.insert(0, 3)
        arr.insert(1, 4)
        arr.insert(3, 5)
        arr.insert(5, 6)
        self.check_array(arr, 16, 6, lst)
        with self.assertRaises(IndexError):
            arr.insert(7, 7)
        with self.assertRaises(IndexError):
            arr.insert(8, 7)
        with self.assertRaises(IndexError):
            arr.insert(-1, 7)
        
    def test_delete_capacity_ok(self):
        arr = DynArray()
        lst = [3, 4, 1, 5, 2, 6]
        arr.append(1)
        arr.insert(1, 2)
        arr.insert(0, 3)
        arr.insert(1, 4)
        arr.insert(3, 5)
        arr.insert(5, 6)
        
        for i in range(16):
            lst.append(i+10)
            arr.append(i+10)
        self.check_array(arr, 32, 22, lst)
            
        arr.delete(0)
        del lst[0]
        self.check_array(arr, 32, 21, lst)
        
        arr.delete(4)
        lst.remove(6)
        self.check_array(arr, 32, 20, lst)
        
        arr.delete(2)
        del lst[2]
        self.check_array(arr, 32, 19, lst)
        
    def test_delete_capacity_rise(self):
        arr = DynArray()
        lst = []
    
        for i in range(0, 32):
            lst.append(i+1)
            arr.append(i+1)
        self.check_array(arr, 32, 32, lst)
        
        for i in range(0, 16):
            arr.delete(i)
            del lst[i]
            self.check_array(arr, 32, 32 - i - 1, lst)
            
        arr.delete(0)
        lst.remove(2)
        self.check_array(arr, 21, 15, lst)
    
    def test_delete_error(self):
        arr = DynArray()
        with self.assertRaises(IndexError):
            arr.delete(0)
        with self.assertRaises(IndexError):
            arr.delete(1)
        with self.assertRaises(IndexError):
            arr.delete(-1)
        lst = [3, 4, 1, 5, 2, 6]
        for x in lst:
            arr.insert(arr.count, x)
        
        with self.assertRaises(IndexError):
            arr.delete(6)
        with self.assertRaises(IndexError):
            arr.delete(-1)
        with self.assertRaises(IndexError):
            arr.delete(7)

if __name__ == '__main__':
    print("BEFORE")
    unittest.main()
