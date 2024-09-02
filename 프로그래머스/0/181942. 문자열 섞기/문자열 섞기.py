# My Code
def solution(str1, str2):
    return ''.join([x1 + x2 for x1, x2 in zip(str1, str2)])