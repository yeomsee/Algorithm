# My Code
def solution(arr, k):
    answer_list = []
    for num in arr:
        if num not in answer_list and len(answer_list) < k:
            answer_list.append(num)
    
    if (left := k - len(answer_list)) != 0:
        for _ in range(left):
            answer_list.append(-1)
    return answer_list
    