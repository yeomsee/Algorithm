# My Code
def solution(n):
    answer = 0
    for i in range(n+1):
        if i%2 == 0:
            answer += i
    
    return answer

# Best Code
def solution2(n):
    return sum([i for i in range(2, n+1, 2)])
