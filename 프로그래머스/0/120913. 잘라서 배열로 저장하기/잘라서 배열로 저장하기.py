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

# Best Code
def solution(my_str, n):
    return [my_str[i: i + n] for i in range(0, len(my_str), n)]

'''
    슬라이싱은 배열의 인덱스를 초과해도 오류 안 남 ㄱㅊㄱㅊ
'''
