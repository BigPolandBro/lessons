def MergeSort_(array: 'list[int]', l, r) -> 'list[int]':
    n = r - l
    if n <= 1:
        return

    md = (l + r)//2
    MergeSort_(array, l, md)
    MergeSort_(array, md, r)

    buffer = array[l:md]
    li, ri = 0, md
    for i in range(l, r):
        if ri >= r or li < len(buffer) and buffer[li] <= array[ri]:
            array[i] = buffer[li]
            li += 1
        else:
            array[i] = array[ri]
            ri += 1

def MergeSort(array):
    MergeSort_(array, 0, len(array))
    return array

