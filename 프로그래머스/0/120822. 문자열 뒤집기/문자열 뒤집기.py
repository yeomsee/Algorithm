# My Code
def solution(my_string):
    answer = ''.join([my_string[i] for i in range(len(my_string)-1, -1, -1)])
    return answer