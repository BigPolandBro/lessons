def swap_elements(M: 'list[int]', i1: int, i2: int, iN: int) -> int:
    M[i1], M[i2] = M[i2], M[i1]
    new_iN = iN
    if i1 == iN:
        new_iN = i2
    if i2 == iN:
        new_iN = i1
    return new_iN


def ArrayChunk(M: 'list[int]', left: int, right: int) -> int:
    iN = (left + right) // 2
    i1 = left
    i2 = right
    while i1 <= i2:
        while M[i1] < M[iN]:
            i1 += 1
        while M[i2] > M[iN]:
            i2 -= 1
        if i1 == i2 - 1 and M[i1] > M[i2]:
            M[i1], M[i2] = M[i2], M[i1]
            iN = ArrayChunk(M, left, right)
            return iN
        if i1 == i2 or (i1 == i2 - 1 and M[i1] < M[i2]):
            return iN
        iN = swap_elements(M, i1, i2, iN)
    return iN


def KthOrderStatisticsStep(Array: 'list[int]', L: int, R: int, k: int) -> 'list[int]':
    iN = ArrayChunk(Array, L, R)
    if iN == k:
        return [iN, iN]
    if iN < k:
        return [iN + 1, R]
    return [L, iN - 1]

