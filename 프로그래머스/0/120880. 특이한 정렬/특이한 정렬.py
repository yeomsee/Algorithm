# My Code
def solution(num_list, n):
    sorted_num_list = sorted(num_list, reverse=True)
    dis_num_list = [(abs(num-n), num) for num in sorted_num_list]
    sorted_dis_num_list = sorted(dis_num_list, key = lambda x : x[0])
    
    return [x for _, x in sorted_dis_num_list]