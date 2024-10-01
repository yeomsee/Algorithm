# My Code
def solution(dots):
    def get_incline(dot1, dot2):
        x1, y1 = dot1
        x2, y2 = dot2
        m = (y2 - y1) / (x2- x1)
        return m
    
    d1, d2, d3, d4 = dots
    if get_incline(d1, d2) == get_incline(d3, d4):
        return 1
    elif get_incline(d1, d3) == get_incline(d2, d4):
        return 1
    elif get_incline(d1, d4) == get_incline(d2, d3):
        return 1
    return 0