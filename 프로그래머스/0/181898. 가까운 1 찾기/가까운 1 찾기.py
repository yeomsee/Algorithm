# My Code
def solution(arr, idx):
    for i in range(len(arr)):
        if arr[i] and i >= idx:
            return i
    return -1