# My Code .. O(n)
def solution(n):
    answer = []
    for i in range(1, n+1):
        if n%i == 0:
            answer.append(i)
    return answer

# Best Code .. O(root(n))
def find(n):
    answer = []
    for i in range(1, int(i**0.5) + 1):
        # n의 제곱근까지만 loop를 돌면서 나누어떨어지는 것들을 append
        if n % i == 0:
            answer.append(i)
            # i와 쌍을 이루는 약수들도 추가
            if i**2 != n:
                answer.append(n // i)
    return answer

def solution(n):
    answer = find(n)
    return sorted(answer)
