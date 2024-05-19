# My Code
def solution(n):
    n = str(n)
    answer = 0
    for x in n:
        answer += int(x)
    return answer

# Best Code(Simpler Ver.)
def solution(n):
    return sum(int(i) for i in str(n))

'''
    내 코드랑 비슷하지만 조금 더 간결해보인다!
'''

# Another Code 
def solution(n):
    answer = 0
    while n:
        answer += n%10
        n //= 10
    return answer
