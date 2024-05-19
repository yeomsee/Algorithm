def solution(money):
    answer = [0, 0]
    price = 5500
    answer[0] = money // price
    answer[1] = money - answer[0] * price
    
    return answer