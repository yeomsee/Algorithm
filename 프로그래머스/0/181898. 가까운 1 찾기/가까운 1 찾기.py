# My Code
def solution(arr, idx):
    for i in range(len(arr)):
        if arr[i] and i >= idx:
            return i
    return -1

# Best Code
def solution(arr, idx):
    answer = 0
    try:
        answer = arr.index(1, idx)
    except:
        answer = -1

    return answer

'''
    list.index(index, start)
'''
