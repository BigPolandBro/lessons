def get_second_maximum_index(numbers_list):
    if len(numbers_list) < 2:
        return -1
        
    mx_val = 0 # assume that every number in numbers_list is positive
    mx_ind = -1 # index of element with maximum value
    for i in range(len(numbers_list)):
        if numbers_list[i] >= mx_val:
            mx_val = numbers_list[i]
            mx_ind = i 
    
    mx_val = 0
    pre_mx_ind = -1 # index of second maximum
    for i in range(len(numbers_list)):
        if i != mx_ind and numbers_list[i] >= mx_val:
            mx_val = numbers_list[i]
            pre_mx_ind = i
    
    return pre_mx_ind
    
def get_second_maximum_index_recursion(numbers_list, mx_ind, cur_ind = 0, pre_mx_ind = -1):
    if cur_ind >= len(numbers_list):
        return pre_mx_ind
    
    if cur_ind != mx_ind and (pre_mx_ind == -1 or numbers_list[cur_ind] >= numbers_list[pre_mx_ind]):
        pre_mx_ind = cur_ind
    
    return get_second_maximum_index_recursion(numbers_list, mx_ind, cur_ind + 1, pre_mx_ind)

def get_second_maximum_index_recursion_run(numbers_list):
    if len(numbers_list) < 2:
        return -1
        
    mx_ind = -1
    for cur_ind in range(len(numbers_list)):
        if mx_ind == -1 or numbers_list[cur_ind] >= numbers_list[mx_ind]:
            mx_ind = cur_ind
    
    return get_second_maximum_index_recursion(numbers_list, mx_ind)
    
def get_second_maximum_index_recursion_no_cycles(numbers_list):
    if len(numbers_list) < 2:
        return None
    
    def helper(numbers_list, cur_ind, mx_ind, pre_mx_ind):
        if cur_ind >= len(numbers_list):
            return pre_mx_ind
        
        if numbers_list[cur_ind] > numbers_list[mx_ind]:
            pre_mx_ind = mx_ind
            mx_ind = cur_ind
        elif numbers_list[cur_ind] > numbers_list[pre_mx_ind]:
                pre_mx_ind = cur_ind
        
        return helper(numbers_list, cur_ind + 1, mx_ind, pre_mx_ind)
    
    mx_ind, pre_mx_ind = 0, 1 
    if numbers_list[mx_ind] < numbers_list[pre_mx_ind]:
        mx_ind, pre_mx_ind = 1, 0
    
    return helper(numbers_list, 2, mx_ind, pre_mx_ind)
    
            
import unittest

class TestTask(unittest.TestCase):
    def test_get_second_maximum_index(self):
        self.assertEqual(get_second_maximum_index([]), -1)
        self.assertEqual(get_second_maximum_index([1]), -1)
        self.assertEqual(get_second_maximum_index([1, 2]), 0)
        self.assertEqual(get_second_maximum_index([1, 1, 1]), 1)
        self.assertEqual(get_second_maximum_index([1, 1, 2, 2]), 2)
        self.assertEqual(get_second_maximum_index([100, 20, 12, 25, 156, 98]), 0)
        
    def test_get_second_maximum_index(self):
        self.assertEqual(get_second_maximum_index_recursion_run([]), -1)
        self.assertEqual(get_second_maximum_index_recursion_run([1]), -1)
        self.assertEqual(get_second_maximum_index_recursion_run([1, 2]), 0)
        self.assertEqual(get_second_maximum_index_recursion_run([1, 1, 1]), 1)
        self.assertEqual(get_second_maximum_index_recursion_run([1, 1, 2, 2]), 2)
        self.assertEqual(get_second_maximum_index_recursion_run([100, 20, 12, 25, 156, 98]), 0)
    
    def test_get_second_maximum_index(self):
        self.assertEqual(get_second_maximum_index_recursion_no_cycles([]), None)
        self.assertEqual(get_second_maximum_index_recursion_no_cycles([1]), None)
        self.assertEqual(get_second_maximum_index_recursion_no_cycles([1, 2]), 0)
        self.assertEqual(get_second_maximum_index_recursion_no_cycles([1, 1, 1]), 1)
        self.assertEqual(get_second_maximum_index_recursion_no_cycles([1, 1, 2, 2]), 3)
        self.assertEqual(get_second_maximum_index_recursion_no_cycles([100, 20, 12, 25, 156, 98]), 0)
        self.assertEqual(get_second_maximum_index_recursion_no_cycles([1, 2, 3, 4, 5]), 3)
        self.assertEqual(get_second_maximum_index_recursion_no_cycles([5, 4, 3, 2, 1]), 1)
    
if __name__ == '__main__':
    print("BEFORE")
    unittest.main()

