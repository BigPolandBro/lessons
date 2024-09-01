def MergeSort(array: 'list[int]') -> 'list[int]':
    n = len(array)
    if n <= 1:
        return array

    md = n // 2
    left = MergeSort(array[0:md])
    right = MergeSort(array[md:n])

    res = list(range(0, n))
    li, ri, i = 0, 0, 0
    ln, rn = len(left), len(right)
    for i in range(0, n):
        if ri >= rn or li < ln and left[li] <= right[ri]:
            res[i] = left[li]
            li += 1
        else:
            res[i] = right[ri]
            ri += 1
    return res


