# My Code
def solution(d, budget):
    d.sort()
    
    count = 0
    for i in d:
        if i <= budget:
            count += 1
            budget -= i
            
    return count

# Best Code
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)
