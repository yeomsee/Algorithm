# My Code
def solution(n):
    for i in range(1, n+1):
        if (6*i)%n == 0:
            answer = i
            break
    return answer

# Simpler Code
def solution(n):
    i=1
    while(1):
        if (6*i)%n==0:
            return i
        i+=1
