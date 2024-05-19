# My Code
def solution(num_list):
    answer = []
    even_count, odd_count = 0, 0
    for num in num_list:
        if num%2 == 0:
            even_count += 1
        else:
            odd_count += 1
    answer.insert(0, even_count)
    answer.insert(1, odd_count)
    return answer

# Best Code
def solution(num_list):
    answer = [0, 0]
    for n in num_list:
        answer[n%2]+=1
    return answer

# Best Code 2
def solution(num_list):
    odd = sum(1 for n in num_list if n % 2)
    return [len(num_list) - odd, odd]
