# My Code
def solution(arr, divisor):
    answer_list = sorted([x for x in arr if x%divisor == 0])
    if len(answer_list) == 0:
        return [-1]
    return answer_list