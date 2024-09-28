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

# Best Code
def solution(quiz):
    answer = []
    for q in quiz:
        L,R = q.split(' = ')
        a,op,b = L.split()
        if op=='+':
            result = 'O' if int(a)+int(b)==int(R) else 'X'
            answer.append(result)
        else:
            result = 'O' if int(a)-int(b)==int(R) else 'X'
            answer.append(result)
    return answer


'''
    현업에서는 eval이 보안상의 이유 때문에 잘 안 쓰인다고해서 eval을 쓰지 않는 코드를 들고옴.
'''
