# My Code
def solution(my_string, n):
    answer = my_string[len(my_string)-n:len(my_string)]
    return answer

# Best Code
def solution(my_string, n):
    return my_string[-n:]
