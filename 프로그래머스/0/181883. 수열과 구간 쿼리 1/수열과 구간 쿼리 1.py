# My Code
def solution(arr, queries):
    for query in queries:
        q1, q2 = query
        
        for i in range(q1, q2+1):
            arr[i] += 1
    return arr