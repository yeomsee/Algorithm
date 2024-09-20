# My Code
def solution(n):
    answer = 0
    for _ in range(n):
        answer += 1
        while True:
            if answer%3 !=0 and '3' not in str(answer):
                break
            answer += 1
    return answer