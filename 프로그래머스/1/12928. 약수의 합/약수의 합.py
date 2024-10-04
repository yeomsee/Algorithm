# My Code
def solution(n):
    answer = []
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            if n//i == i:
                answer.append(i)
            else:
                answer.extend([i, n//i])
            
    return sum(answer)