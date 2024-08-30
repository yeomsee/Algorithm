# My Code
def solution(arr):
    answer = []
    for num in arr:
        if num%2 == 0 and num >= 50:
            answer.append(num/2)
        elif num%2 != 0 and num < 50:
            answer.append(num*2)
        else:
            answer.append(num)
    return answer