# My Code
def solution(my_string):
    my_string = list(my_string.lower())
    my_string.sort()
    
    return ''.join(my_string)