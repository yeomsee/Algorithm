# My Code
def solution(string):
    if (len(string)==4 or len(string)==6) and all(s.isdigit() for s in string):
        return True
    return False