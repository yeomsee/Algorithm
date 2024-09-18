# My Code
def solution(ranks, attendances):
    temp_list = [rank for rank, attendance in zip(ranks, attendances) if attendance == True]
    a, b, c = sorted(temp_list)[:3]
    a, b, c = ranks.index(a), ranks.index(b), ranks.index(c)
    
    return 10000*a + 100*b + c

# Best Code
def solution(rank, attendance):
    arr = sorted([(x, i) for i, x in enumerate(rank) if attendance[i]])
    return arr[0][1] * 10000 + arr[1][1] * 100 + arr[2][1]
