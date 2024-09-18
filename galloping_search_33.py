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

        Mid = (self.Right + self.Left) // 2
        if self.Array[Mid] == N:
            self.Status = 1
            return

        if self.Array[Mid] < N:
            self.Left = Mid + 1
        else:
            self.Right = Mid - 1

        if abs(self.Left - self.Right) <= 1:
            if self.Left <= self.Right and N in (self.Array[self.Left], self.Array[self.Right]):
                self.Status = 1
            else:
                self.Status = -1
            return

    def GetResult(self) -> int:
        return self.Status

    def GallopingSearch(self, array: 'list[int]', N: int) -> bool:
        size = len(array)
        if size == 0 or array[0] > N or array[size - 1] < N:
            return False

        if array[0] == N:
            return True

        i = 1
        cur_index = 2 ** i - 2

        while cur_index < size - 1 and array[cur_index] <= N:
            if array[cur_index] == N:
                return True

            i += 1
            cur_index = min(2**i - 2, size - 1)

        self.Array = array
        self.Left = (2**(i-1) - 2) + 1
        self.Right = cur_index
        self.Status = 0
        while self.GetResult() == 0:
            self.Step(N)
        return self.GetResult() == 1



