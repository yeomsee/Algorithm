# My Code
def solution(num):
    i = 0
    while num != 1:
        num = num/2 if num%2 == 0 else (num*3 + 1)
        
        i += 1
        if i == 500:
            return -1
        
    return i