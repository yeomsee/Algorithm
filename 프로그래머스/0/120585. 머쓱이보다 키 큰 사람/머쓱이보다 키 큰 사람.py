# My Code
def solution(array, height):
    answer = len([x for x in array if x > height])
    
    return answer

# Similar Code
def solution(array, height):
    return sum(1 for a in array if a > height)
