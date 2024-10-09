# My Code
def solution(string):
    return (len(string)==4 or len(string)==6) and all(s.isdigit() for s in string)

# Simpler Code
def alpha_string46(s):
    return s.isdigit() and len(s) in [4,6]
