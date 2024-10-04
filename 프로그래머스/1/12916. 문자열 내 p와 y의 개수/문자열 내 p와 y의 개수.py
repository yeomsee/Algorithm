# My Code
def solution(string):
    string = string.lower() # lower 함수는 할당을 받아야 함
    
    if (string.count('p') == 0) and (string.count('y') == 0):
        return True
    return string.count('p') == string.count('y')

# Simpler Code
def solution(string):
    return string.lower().count('p') == string.lower().count('y')
