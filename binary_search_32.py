class BinarySearch:
    def __init__(self, array: 'list[int]') -> None:
        self.Array = array
        self.Left = 0
        self.Right = len(array) - 1
        self.Status = 0
        self.Index = -1

    def Step(self, N: int) -> None:
        if self.Status != 0:
            return

        if self.Left > self.Right:
            self.Status = -1
            return

        if self.Left in (self.Right, self.Right - 1):
            if N in (self.Array[self.Left], self.Array[self.Right]):
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

    def GetResult(self) -> int:
        return self.Status




