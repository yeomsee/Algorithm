# My Code
def solution(my_string):
    answer = ''
    for string in my_string:
        if (string.isdigit()): # isdigit() 적극적으로 활용자
            answer += string
        else:
            answer += ' '
    
    sum = 0
    for num in answer.split():
        sum += int(num)
    return sum

# Simpler Code
def solution(my_string):
    s = ''.join(i if i.isdigit() else ' ' for i in my_string)
    return sum(int(i) for i in s.split())

# 정규표현식 사용하기
import re

def solution(my_string):
    return sum([int(i) for i in re.findall(r'[0-9]+', my_string)])

'''
    re.findall(r'[0-9]+', my_string) 설명
    my_string에서 r'[0-9]+'를 통해 하나 이상의 연속된 숫자를 찾음.
'''
