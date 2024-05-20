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