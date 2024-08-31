# My Code
def solution(arr, k):
    answer = [
        num*k if k%2 != 0 else num+k
        for num in arr
    ]
    return answer