# My Code
def solution(my_string, n):
    answer = ''
    for string in my_string:
        answer += string*n
    
    return answer

# Best Code
def solution(my_string, n):
    return ''.join(i*n for i in my_string)

'''
    join을 활용해서 효율적으로 만들 수도 있음.
'''
