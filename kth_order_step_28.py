def ArrayChunk(array: 'list[int]', left: int, right: int) -> int:
    if left > right:
        return -1

    pivot_ind = (left + right) // 2
    pivot = array[pivot_ind]
    array[pivot_ind], array[right] = array[right], array[pivot_ind]
    i = left - 1
    for j in range(left, right):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[right] = array[right], array[i + 1]
    return i + 1


def KthOrderStatisticsStep(Array: 'list[int]', L: int, R: int, k: int) -> 'list[int]':
    iN = ArrayChunk(Array, L, R)
    if iN == k:
        return [iN, iN]
    if iN < k:
        return [iN + 1, R]
    return [L, iN - 1]

