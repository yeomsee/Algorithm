# My Code .. 시간복잡도는 꽤 있는 듯
def solution(n):
    answer = []
    for i in range(1, n+1):
        if n%i == 0:
            answer.append(i)
    return answer