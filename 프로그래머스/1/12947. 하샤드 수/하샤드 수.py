# My Code
def solution(x):
    hap = sum([int(s) for s in str(x)])

    return (x%hap == 0)