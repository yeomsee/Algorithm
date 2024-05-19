# My Code
def solution(sides):
    sides.sort()
    s, m, l = sides[0], sides[1], sides[2] # small, medium, large
    
    if l < (s+m): # 삼각형 형성 조건
        answer = 1
    else:
        answer = 2
        
    return answer

# Another Code : Simpler Code
def solution(sides):
    sides.sort()
    return 1 if sides[0]+sides[1]>sides[2] else 2

# Best Code
def solution(sides):
    return 1 if max(sides) < (sum(sides) - max(sides)) else 2

