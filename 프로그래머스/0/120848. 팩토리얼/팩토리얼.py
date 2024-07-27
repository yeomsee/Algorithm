# My Code
def solution(n):
    answer,  i = 1, 1
    while True:
        if answer * (i+1) > n:
            return i
        i += 1
        answer *= i