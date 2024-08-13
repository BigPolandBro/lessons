def swap_elements(M, i1, i2, iN):
    M[i1], M[i2] = M[i2], M[i1]
    new_iN = iN
    if i1 == iN:
        new_iN = i2 
    if i2 == iN:
        new_iN = i1
    return new_iN

def ArrayChunk(M):
    iN = len(M)//2
    i1 = 0
    i2 = len(M) - 1
    while i1 <= i2:
        while M[i1] < M[iN]:
            i1 += 1 
        while M[i2] > M[iN]:
            i2 -= 1 
        if i1 == i2 - 1 and M[i1] > M[i2]:
            M[i1], M[i2] = M[i2], M[i1]
            iN = ArrayChunk(M)
            return iN
        if i1 == i2 or (i1 == i2 - 1 and M[i1] < M[i2]):
            return iN 
        iN = swap_elements(M, i1, i2, iN)
    return iN


