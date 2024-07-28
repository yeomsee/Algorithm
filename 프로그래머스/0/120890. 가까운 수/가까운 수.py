# My Code
def solution(array, n):
    dist_list = [abs(num - n) for num in array]
    min_dist = min(dist_list) # dist_list.min()는 아님에 주의!
    min_idx_list = [idx for idx, val in enumerate(dist_list) if val == min_dist]
    
    answer_list = []
    for i in min_idx_list:
        if len(min_idx_list) == 1:
            return array[i]
        else:
            answer_list.append(array[i])
    return min(answer_list)