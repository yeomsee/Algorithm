# My Code
def solution(my_string, m, c):
    answer = ''
    for i in range(0, len(my_string), m):
        temp_string = my_string[i:i+m]
        answer += temp_string[c-1]
    
    return answer