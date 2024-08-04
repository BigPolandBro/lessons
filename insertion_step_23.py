def InsertionSortStep(array, step, i):
    n = len(array)
    for j in range(i+step, n, step):
        first_bigger = j + 1
        for k in range(i, j, step):
            if array[j] < array[k]:
                first_bigger = k 
                break
        for k in range(j, first_bigger, -step):
            array[k], array[k-step] = array[k-step], array[k]


