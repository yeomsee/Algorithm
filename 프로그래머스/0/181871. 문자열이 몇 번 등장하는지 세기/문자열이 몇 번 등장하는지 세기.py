# My Code
def solution(my_string, pat):
    count = 0
    for i in range(len(my_string)):
        if my_string[i:i+len(pat)] == pat:
            count += 1
            
    return count