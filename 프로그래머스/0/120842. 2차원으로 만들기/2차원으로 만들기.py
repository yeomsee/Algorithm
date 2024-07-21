# My Code
def solution(num_list, n):
    answer_list = []
    for i in range(0, len(num_list)+1, n):
        if i >= len(num_list)-1:
            break
        answer_list.append(num_list[i:i+n])
    return answer_list