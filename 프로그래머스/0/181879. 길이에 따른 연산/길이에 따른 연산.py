# My Code
def solution(num_list):
    def multiply(num_list):
        ret = 1
        for num in num_list:
            ret *= num
        return ret

    answer = sum(num_list) if len(num_list) >= 11 else multiply(num_list)
    return answer

# Best Code
def solution(num_list):
    if len(num_list) >= 11:
        return eval('+'.join(list(map(str, num_list))))
    else:
        return eval('*'.join(list(map(str, num_list))))

'''
    * map(function, iterable)
    : iterable한 객체 안에 있는 모든 요소들에 대해 function을 적용

    * eval(expression : str)
    : expression을 받아서 파이썬이 알아서 실행해주는 함수
'''

# Another Code
from math import prod

def solution(num_list):
    return sum(num_list) if len(num_list)>=11 else prod(num_list)
