# My Code
def solution(money):
    answer = [0, 0]
    price = 5500
    answer[0] = money // price
    answer[1] = money - answer[0] * price
    
    return answer

# BEST Code
def solution(money):

    answer = [money // 5500, money % 5500]
    return answer
