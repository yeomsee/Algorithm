# My Code
def solution(str_list, ex):
    answer = ''.join([string for string in str_list if ex not in string])
    return answer

'''
    list comprehension
    else가 없으면 for - if
    else가 있으면 if-else-for
'''