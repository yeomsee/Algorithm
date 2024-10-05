# My Code
def solution(n):
    return [int(s) for s in str(n)][::-1]

# Best Code
def digit_reverse(n):
    return list(map(int, reversed(str(n))))
