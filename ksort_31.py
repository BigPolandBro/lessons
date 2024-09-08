class ksort:
    def __init__(self):
        self.letters = "abcdefgh"
        self.size = 100*len(self.letters)
        self.items = [None for _ in range(self.size)]

    def check_format(self, s):
        return len(s) == 3 and s[0] in self.letters and s[1].isdigit() and s[2].isdigit()

    def index(self, s):
        if not self.check_format(s):
            return -1
        return (ord(s[0]) - ord('a'))*100 + int(s[1:3])

    def add(self, s):
        index = self.index(s)
        if index == -1:
            return False
        self.items[index] = s
        return True



