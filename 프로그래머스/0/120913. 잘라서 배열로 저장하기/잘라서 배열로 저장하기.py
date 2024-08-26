# My Code
def solution(my_str, n):
    answer = []
    
    i = 0
    while i <= len(my_str)-1:
        if i + (n-1) >= len(my_str):
            answer.append(my_str[i:len(my_str)])
            break
        else:
            answer.append(my_str[i:i+n])
        
        i += n
    
    return answer