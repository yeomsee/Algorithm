# My Code
def solution(numbers, k):
    turn, count = 0, 0
    while True:
        count += 1
        if count == k:
            return numbers[turn % len(numbers)]
        turn += 2
        
            