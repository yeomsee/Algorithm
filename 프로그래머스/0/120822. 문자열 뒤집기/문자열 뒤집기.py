# My Code
def solution(my_string):
    answer = ''.join([my_string[i] for i in range(len(my_string)-1, -1, -1)])
    return answer

# Best Code
def solution(my_string):
    return my_string[::-1]

'''
    지난 번에 봤던 코드,, 다시 한 번 잘 새기자
'''
