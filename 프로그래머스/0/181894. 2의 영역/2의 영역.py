# My Code
def solution(arr):
    for i in range(len(arr)):
        if arr[i] == 2:
            for j in range(len(arr)-1, i-1, -1):
                if arr[j] == 2:
                    return arr[i:j+1]
    return [-1]