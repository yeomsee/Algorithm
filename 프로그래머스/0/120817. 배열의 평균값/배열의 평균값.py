# My Code
def solution(number_list):
    sum = 0
    for number in number_list:
        sum += number
    answer = sum / len(number_list)

    return answer

# Best Code
def solution(numbers):
    return sum(numbers) / len(numbers)
