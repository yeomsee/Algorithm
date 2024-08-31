# My Code
def solution(rny_string):
    return ''.join(['rn' if string == 'm' else string for string in rny_string])

# Best Code
def solution(rny_string):
    return rny_string.replace('m', 'rn')

'''
    replace 함수를 이용한 깔끔한 풀이,,!
'''
