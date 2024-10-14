# My Code
def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i < len(arr)-1:
            if arr[i] == arr[i+1]:
                continue
        answer.append(arr[i])
    return answer