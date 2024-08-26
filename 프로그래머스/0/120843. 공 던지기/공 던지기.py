# My Code
def solution(numbers, k):
    turn, count = 0, 0
    while True:
        count += 1
        if count == k:
            return numbers[turn % len(numbers)]
        turn += 2
        
# Best Code
def solution(numbers, k):
    return numbers[2 * (k - 1) % len(numbers)]

'''
    이게 훨씬 더 직관적인 듯,,
'''
