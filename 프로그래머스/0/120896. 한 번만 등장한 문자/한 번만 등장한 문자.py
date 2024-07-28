# My Code
def solution(s):
    answer = ''
    s = sorted(s)
    
    for string in s:
        if s.count(string) == 1:
            answer += string
            
    return answer