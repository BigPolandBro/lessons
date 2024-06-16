class aBST:

    def __init__(self, depth):
        tree_size = 2**(depth+1) - 1
        self.Tree = [None] * tree_size
	
    def FindKeyIndex(self, key):
        def helper(index, key):
            if index >= len(self.Tree):
                return None
            if self.Tree[index] is None:
                return -index
            if self.Tree[index] == key:
                return index 
                
            if key < self.Tree[index]:
                index = index*2 + 1 
            else:
                index = index*2 + 2
            return helper(index, key)
        return helper(0, key) 
	
    def AddKey(self, key):
        index = self.FindKeyIndex(key)
        if index is None:
            return -1
        if (index == 0 and self.Tree[index] is None) or index < 0:
            index *= -1
            self.Tree[index] = key
        return index



