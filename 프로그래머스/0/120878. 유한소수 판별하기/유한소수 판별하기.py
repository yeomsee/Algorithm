# My Code
def solution(a, b):
    def get_gcd(a, b):
        for i in range(min(a, b), 0, -1):
            if a%i == 0 and b%i == 0:
                return i
            
    gcd = get_gcd(a, b)
    b = int(b/gcd)
    
    for x in range(2, b+1):
        if (b%x == 0) and (x%2 != 0 and x%5 != 0):
            return 2
    return 1

'''
    기억하자!
    파이썬에서 나누기 연산의 return 값은 무.조.건. 실수형이다!
'''

# Simpler Code
from math import gcd
def solution(a, b):
    b //= gcd(a,b)
    while b%2==0:
        b//=2
    while b%5==0:
        b//=5
    return 1 if b==1 else 2
