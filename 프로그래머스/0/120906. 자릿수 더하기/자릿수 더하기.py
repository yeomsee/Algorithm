def solution(n):
    n = str(n)
    answer = 0
    for x in n:
        answer += int(x)
    return answer