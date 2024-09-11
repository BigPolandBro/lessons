class BinarySearch:
    def __init__(self, array):
        self.Array = array
        self.Left = 0
        self.Right = len(array) - 1
        self.Status = 0
        self.Index = -1

    def Step(self, N):
        if self.Status != 0:
            return

        if self.Left > self.Right:
            self.Status = -1
            return

        if self.Left == self.Right or self.Left == self.Right - 1:
            if self.Array[self.Left] == N or self.Array[self.Right] == N:
                self.Status = 1
            else:
                self.Status = -1
            return

        Mid = (self.Right + self.Left) // 2
        if self.Array[Mid] == N:
            self.Status = 1
            return

        if self.Array[Mid] < N:
            self.Left = Mid + 1
        else:
            self.Right = Mid - 1

    def GetResult(self):
        return self.Status




