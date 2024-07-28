# My Code
def solution(i, j, k):
    answer = sum([str(num).count(str(k)) for num in range(i, j+1) if str(k) in str(num)])
    
    return answer