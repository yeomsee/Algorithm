# My Code
def solution(n):
    temp_list = sorted([int(s) for s in str(n)], reverse=True)
    temp_list = map(str, temp_list)
    
    return int(''.join(temp_list))