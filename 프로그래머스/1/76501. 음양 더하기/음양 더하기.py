# My Code
def solution(absolutes, signs):        
    return sum([num if sign == True else -num for num, sign in zip(absolutes, signs)])