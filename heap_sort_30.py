class Heap:

    def __init__(self):
        self.HeapArray = []
        self.heap_size = 0
        self.n = 0

    def MakeHeap(self, a, depth):
        self.heap_size = 2 ** (depth + 1) - 1
        self.HeapArray = [-1 for i in range(self.heap_size)]
        self.n = len(a)
        for i in range(0, self.n):
            self.HeapArray[i] = a[i]
        for i in range(self.n // 2 - 1, -1, -1):
            self.heapify_down(i)

    def heapify_down(self, ind):
        if ind > self.heap_size // 2 - 1:
            return

        left_ind = ind * 2 + 1
        right_ind = ind * 2 + 2
        left_tuple = (self.HeapArray[left_ind], left_ind)
        right_tuple = (self.HeapArray[right_ind], right_ind)
        max_tuple = max(left_tuple, right_tuple)

        if self.HeapArray[ind] < max_tuple[0]:
            next_ind = max_tuple[1]
            self.HeapArray[ind], self.HeapArray[next_ind] = self.HeapArray[next_ind], self.HeapArray[ind]
            self.heapify_down(next_ind)

    def heapify_up(self, ind):
        if ind <= 0:
            return

        next_ind = ind // 2
        if ind % 2 == 0:
            next_ind -= 1

        if self.HeapArray[next_ind] < self.HeapArray[ind]:
            self.HeapArray[ind], self.HeapArray[next_ind] = self.HeapArray[next_ind], self.HeapArray[ind]
            self.heapify_up(next_ind)

    def check_heap(self):
        for i in range(0, self.heap_size // 2):
            if self.HeapArray[i] < self.HeapArray[i * 2 + 1] or self.HeapArray[i] < self.HeapArray[i * 2 + 2]:
                return False
        return True

    def GetMax(self):
        if self.heap_size <= 0 or self.n <= 0:
            return -1
        mx = self.HeapArray[0]
        ind_last = self.n - 1
        self.HeapArray[0] = self.HeapArray[ind_last]
        self.HeapArray[ind_last] = -1
        self.n -= 1
        self.heapify_down(0)
        return mx

    def Add(self, key):
        if self.heap_size <= self.n:
            return False
        ind_last = self.n
        self.HeapArray[ind_last] = key
        self.n += 1
        self.heapify_up(ind_last)
        return True

class HeapSort:
    def __init__(self, array : 'list[int]') -> None:
        self.HeapObject = Heap()
        depth = 0
        n = len(array)
        for i in range(0, n + 1):
            if 2 ** (i + 1) - 1 >= n:
                depth = i
                break

        self.HeapObject.MakeHeap([], depth)
        for i in range(n):
            self.HeapObject.Add(array[i])

    def GetNextMax(self) -> int:
        return self.HeapObject.GetMax()



