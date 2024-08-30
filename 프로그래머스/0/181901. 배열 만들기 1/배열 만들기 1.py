# My Code
def solution(n, k):
    answer = list(sorted([i for i in range(1, n+1) if i%k == 0]))
    return answer