# My Code
def solution(my_string, pat):
    N = len(pat)
    for i in range(len(my_string)):
        temp_string = my_string[len(my_string)-i-N:len(my_string)-i]
        if temp_string == pat:
            return my_string[:len(my_string)-i]