# My code
def solution(n):
    answer = 1 if (int(n**0.5))**2 == n else 2
    return answer

'''
    ** 연산자 인자에 1/2이 들어가도 괜찮음!
'''

# Another Code
def solution(n):
    return 1 if (n ** 0.5).is_integer() else 2

'''
    is_integer() 함수를 이용
'''
