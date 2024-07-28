# My Code
def solution(array):
    answer = sum([str(num).count("7") for num in array])
    return answer