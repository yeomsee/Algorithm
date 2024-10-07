# My Code
def solution(s):
    n = len(s)
    if n%2 != 0:
        return s[n//2]
    return s[n//2-1] + s[n//2]

# Simpler Code
def string_middle(str):
    return str[(len(str)-1)//2 : len(str)//2 + 1]
