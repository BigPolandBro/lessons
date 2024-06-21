def GenerateBBSTArray(a: 'list[int]') -> 'list[int]':
    n = len(a)
    if n == 0:
        return []
    a = sorted(a)
    b = [i for i in range(n)]
    
    def helper(ind: int, lb: int, rb: int) -> None:
        mid = (lb + rb) // 2
        b[ind] = a[mid]
        if mid == lb:
            return
        helper(ind*2 + 1, lb, mid - 1) 
        helper(ind*2 + 2, mid + 1, rb)
        
    helper(0, 0, n-1)
    return b


