class NativeDictionary:
    def __init__(self, sz):
        self.step = 1
        self.X = 241
        self.M = 1000000087
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        hash = 0 
        for c in key:
            cur = ord(c) - ord('a') + 1
            hash = (hash * self.X + cur) % self.M
        return hash % self.size
   
    def seek_slot(self, key):
        start = self.hash_fun(key)
        ind = start
        while self.slots[ind] is not None:
            ind = (ind + self.step) % self.size
            if ind == start:
                break
        if self.slots[ind] is not None:
            return None
        return ind
   
    def find(self, key):
        start = self.hash_fun(key)
        ind = start
        while self.slots[ind] != key:
            ind = (ind + self.step) % self.size
            if ind == start:
                break
        if self.slots[ind] != key:
            return None
        return ind

    def put(self, key, value):
        ind = self.find(key)
        if ind is None:
            ind = self.seek_slot(key)
        self.slots[ind] = key 
        self.values[ind] = value
        
    def is_key(self, key):
        return self.find(key) is not None

    def get(self, key):
        ind = self.find(key)
        if ind is None:
            return None
        return self.values[ind]

