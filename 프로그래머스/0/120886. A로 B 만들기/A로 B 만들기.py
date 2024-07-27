# My Code
def solution(before, after):
    before, after = list(before), list(after)
    before.sort()
    after.sort()
    
    if before == after:
        return 1
    return 0