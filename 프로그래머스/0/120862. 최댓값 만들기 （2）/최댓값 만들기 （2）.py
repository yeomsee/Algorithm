def solution(numbers):
    numbers.sort()
    x1, x2, x3, x4 = numbers[0], numbers[1], numbers[-1], numbers[-2]
    answer = x1*x2 if x1*x2 > x3*x4 else x3*x4
    
    return answer