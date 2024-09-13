# My Code
def solution(arr):
    i = 0
    stk = []
    while i < len(arr):
        if len(stk) == 0:
            stk.append(arr[i])
            i += 1
            continue
        else:
            if stk[-1] < arr[i]:
                stk.append(arr[i])
                i += 1
            else:
                stk.pop(-1)
    return stk