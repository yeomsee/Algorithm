# My Code
def solution(n):
    # 소수인지를 체크하는 함수
    def check_prime_num(num):
        count = 0
        for x in range(2, num+1):
            if num%x == 0:
                count += 1
            if count >= 2:
                return False
        return True
    
    answer_list = []
    for i in range(2, n+1):
        # 약수인 경우 + 그 약수가 소수인 경우 answer_list에 append
        if n%i == 0 and check_prime_num(i):
            answer_list.append(i)
    answer_list.sort()
    
    return answer_list

# Best Code
def solution(n):
    answer = []
    d = 2
    while d <= n:
        if n % d == 0:
            n /= d
            if d not in answer:
                answer.append(d)
        else:
            d += 1
    return answer
