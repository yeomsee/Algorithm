# My Code
def solution(a, b):
    m, M = min([a,b]), max([a, b])
    return sum([x for x in range(m, M+1)])