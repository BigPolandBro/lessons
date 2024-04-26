class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size
        self.X = 241
        self.M = 1000000087

    def hash_fun(self, value):
        hash = 0 
        for c in value:
            cur = ord(c) - ord('a') + 1
            hash = (hash * self.X + cur) % self.M
        return hash % self.size

    def seek_slot(self, value):
        start = self.hash_fun(value)
        ind = start
        while self.slots[ind] is not None:
            ind = (ind + self.step) % self.size
            if ind == start:
                break
        if self.slots[ind] is not None:
            return None
        return ind

    def put(self, value):
        ind = self.seek_slot(value)
        if ind is None:
            return None
        self.slots[ind] = value
        return ind

    def find(self, value):
        start = self.hash_fun(value)
        ind = start
        while self.slots[ind] != value:
            ind = (ind + self.step) % self.size
            if ind == start:
                break
        if self.slots[ind] != value:
            return None
        return ind

