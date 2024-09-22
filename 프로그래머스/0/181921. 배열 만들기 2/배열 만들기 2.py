# My Code
def solution(l, r):
    answer = []
    for num in range(l, r+1):
        if all(x=="0" or x=="5" for x in str(num)):
            answer.append(num)

    if len(answer) == 0:
        return [-1]
    return answer
        
    