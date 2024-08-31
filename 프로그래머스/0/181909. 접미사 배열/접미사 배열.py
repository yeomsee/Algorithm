# My Code
def solution(my_string):
    answer = [my_string[len(my_string)-1-i:] for i in range(len(my_string))]
    answer.sort()
    return answer