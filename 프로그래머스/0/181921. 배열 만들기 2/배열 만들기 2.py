# My Code
def solution(l, r):
    answer = []
    for num in range(l, r+1):
        if all(x=="0" or x=="5" for x in str(num)):
            answer.append(num)

    if len(answer) == 0:
        return [-1]
    return answer

# Best Code
def solution(l, r):
    answer = []
    for num in range(l, r + 1):
        if not set(str(num)) - set(['0', '5']):
            answer.append(num)
    return answer if answer else [-1]

'''
    set을 이용해볼까도 당연히 생각봤는데,, 차집합의 개념을 이용하면 이렇게 깔끔하게 풀 수 있다는 것도 배웠다. 굿!
'''
