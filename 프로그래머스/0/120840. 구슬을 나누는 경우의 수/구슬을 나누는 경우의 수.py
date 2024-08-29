# My Code
def solution(balls, share):
    def get_factorial(n):
        result = 1
        for i in range(n, 1, -1):
            result *= i
        return result
    
    answer = get_factorial(balls) / (get_factorial(share) * get_factorial(balls - share))
    return answer

# Another Code
import math

def solution(balls, share):
    return math.comb(balls, share)

'''
    math 라이브러리를 import해서 푸는 경우도 있음!
'''
