# My Code
def solution(arr, flags):
    answer = []
    for num, flag in zip(arr, flags):
        if flag == True:
            for i in range(num*2):
                answer.append(num)
        else:
            for i in range(num):
                answer.pop()
                
    return answer