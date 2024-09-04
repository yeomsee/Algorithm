# My Code
def solution(arr, queries):
    for query in queries:
        q1, q2 = query
        arr[q1], arr[q2] = arr[q2], arr[q1]

    return arr