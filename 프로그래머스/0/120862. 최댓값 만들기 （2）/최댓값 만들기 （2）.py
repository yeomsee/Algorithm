# My Code
def solution(numbers):
    numbers.sort()
    x1, x2, x3, x4 = numbers[0], numbers[1], numbers[-1], numbers[-2]
    answer = x1*x2 if x1*x2 > x3*x4 else x3*x4
    
    return answer

# Best Code (Similar Ver.)
def solution(numbers):
    numbers.sort()
    return max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])

# Another Code
from itertools  import combinations as comb

def solution(numbers):
    an_list=[]
    for i,j in comb(numbers,2):
        an_list.append(i*j)
    return max(an_list)
