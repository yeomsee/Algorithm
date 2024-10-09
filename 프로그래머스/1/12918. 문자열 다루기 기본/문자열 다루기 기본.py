# My Code
def solution(string):
    return (len(string)==4 or len(string)==6) and all(s.isdigit() for s in string)