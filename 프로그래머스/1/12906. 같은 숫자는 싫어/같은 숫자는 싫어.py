# My Code
def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i < len(arr)-1:
            if arr[i] == arr[i+1]:
                continue
        answer.append(arr[i])
    return answer

# Best Code
def no_continuous(s):
    a=[v for i,v in enumerate(s) if s[i-1]!=s[i]]
    return a
