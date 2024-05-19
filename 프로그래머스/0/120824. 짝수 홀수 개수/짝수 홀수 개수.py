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