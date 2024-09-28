# My Code
def solution(quiz):
    answer = []
    for q in quiz:
        l, r = q.split("=")
        if eval(l) == eval(r):
            answer.append("O")
        else:
            answer.append("X")

    return answer