def ArrayChunk(M, left, right):
    if left > right:
        return -1
    N = M[right]
    i = left - 1
    for j in range(left, right):
        if M[j] <= N:
            i += 1
            M[i], M[j] = M[j], M[i]
    M[i+1], M[right] = M[right], M[i+1]
    return i+1

def QuickSortTailOptimization(array, left, right):
    def start():
        nonlocal left, right
        if left >= right:
            return
        
        iN = ArrayChunk(array, left, right)
        if iN - left < right - iN:
            QuickSortTailOptimization(array, left, iN - 1)
            left = iN + 1 
        else:
            QuickSortTailOptimization(array, iN + 1, right)
            right = iN - 1
            
        start()
        
    start()



