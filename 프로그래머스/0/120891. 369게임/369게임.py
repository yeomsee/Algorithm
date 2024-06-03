# My Code
def solution(order):
    answer = 0
    
    order = str(order)
    for num in order:
        if num == "3" or num == "6" or num == "9":
            answer += 1
    return answer

'''
    원래는 if int(num)%3 == 0 이라고 썼는데 num이 "0"인 경우는 고려하지 않았다.
    int(num) != 0 까지 썼으면 돌아갔을 듯.
'''
