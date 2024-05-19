def solution(sides):
    sides.sort()
    s, m, l = sides[0], sides[1], sides[2]
    
    if l < (s+m):
        answer = 1
    else:
        answer = 2
        
    return answer