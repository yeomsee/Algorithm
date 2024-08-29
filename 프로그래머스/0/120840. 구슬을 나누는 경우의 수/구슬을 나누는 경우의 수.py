# My Code
def solution(balls, share):
    def get_factorial(n):
        result = 1
        for i in range(n, 1, -1):
            result *= i
        return result
    
    answer = get_factorial(balls) / (get_factorial(share) * get_factorial(balls - share))
    return answer