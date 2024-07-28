# My Code
def solution(s):
    s = s.split()
    for i in range(len(s)):
        if s[i] == "Z":
            s[i] = -int(s[i-1])
    
    answer = sum([int(num) for num in s])
    return answer