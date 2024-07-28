# My Code
def solution(s):
    answer = ''
    s = sorted(s)
    
    for string in s:
        if s.count(string) == 1:
            answer += string
            
    return answer

# Simpler Code
def solution(s):
    answer = "".join(sorted([ch for ch in s if s.count(ch) == 1]))
    return answer
