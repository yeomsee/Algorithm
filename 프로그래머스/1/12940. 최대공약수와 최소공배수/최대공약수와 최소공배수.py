# My Code
def solution(n, m):
    m, M = min(n, m), max(n, m)
    
    temp_list = []
    for i in range(1, int(m**0.5) + 1):
         if m%i == 0:
            temp_list.extend([i, m//i])
    
    for x in sorted(temp_list, reverse=True):
        if M%x == 0:
            gcd = x
            lcm = gcd * (M//x) * (m//x)
            return [gcd, lcm]

# Best Code
def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)

''' 최대공약수 구하는 법
    -> 유클리드 호제법 : 두 수의 나머지를 반복적으로 구하면서 나머지가 0이 될 때의 나누는 수가 최대공약수
'''

def lcm(a, b):
    return a * b // gcd(a, b)

def gcdlcm(a, b):
    answer = [gcd(a, b), lcm(a, b)]
    return answer
