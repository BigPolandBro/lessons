def KnuthSequence(array_size: int) -> 'list[int]':
    i = 1
    seq = []
    while i < array_size:
        seq.append(i)
        i = i*3 + 1
    seq.reverse()
    return seq


def InsertionSortStep(array: 'list[int]', step: int, i: int) -> None:
    n = len(array)
    for j in range(i + step, n, step):
        first_bigger = j + 1
        for k in range(i, j, step):
            if array[j] < array[k]:
                first_bigger = k
                break
        for k in range(j, first_bigger, -step):
            array[k], array[k - step] = array[k - step], array[k]


def ShellSort(array: 'list[int]') -> None:
    seq = KnuthSequence(len(array))
    for step in seq:
        for i in range(0, step):
            InsertionSortStep(array, step, i)

