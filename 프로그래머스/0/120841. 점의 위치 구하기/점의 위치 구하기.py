# My Code
def solution(dot):
    x, y = dot[0], dot[1]
    if x > 0:
        if y > 0:
            answer = 1
        elif y < 0:
            answer = 4
    elif x < 0:
        if y > 0:
            answer = 2
        elif y < 0:
            answer = 3
    return answer

# Another Code(Simpler Ver.)
def solution(dot):
    x,y = dot
    if x*y>0:
        return 1 if x>0 else 3
    else:
        return 4 if x>0 else 2

'''
    x, y = dot[0], dot[1]
    x, y = dot
    => 같은 결과!
'''
