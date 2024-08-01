def SelectionSortStep(array, i):
    if i >= len(array):
        return
    ind_min = i
    for j in range(i+1, len(array)):
        if array[j] < array[ind_min]:
            ind_min = j
    if i != ind_min:
        array[i], array[ind_min] = array[ind_min], array[i]
    

def BubbleSortStep(array):
    flag = True
    for i in range(len(array) - 1):
        if array[i] > array[i+1]:
            flag = False
            array[i], array[i+1] = array[i+1], array[i]
    return flag



