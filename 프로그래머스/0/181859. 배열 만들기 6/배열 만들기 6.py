# My Code
def solution(arr):
    i = 0
    stk = []
    while i < len(arr):
        if len(stk) == 0:
            stk.append(arr[i])
            i += 1
        else:
            if stk[-1] == arr[i]:
                stk.pop(-1)
                i += 1
            else:
                stk.append(arr[i])
                i += 1     
                
    if len(stk) == 0:
        return [-1]
    return stk