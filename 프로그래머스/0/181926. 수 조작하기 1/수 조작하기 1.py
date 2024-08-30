# My Code
def solution(n, control):
    control_dict = {"w" : 1, "s" : -1, "d" : 10, "a" : -10}
    
    answer = n + sum(control_dict[c] for c in control)
    return answer

# Simpler Code
def solution(n, control):
    key = dict(zip(['w','s','d','a'], [1,-1,10,-10]))
    return n + sum([key[c] for c in control])
