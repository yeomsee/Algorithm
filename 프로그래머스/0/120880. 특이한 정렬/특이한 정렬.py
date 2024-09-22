# My Code
def solution(num_list, n):
    sorted_num_list = sorted(num_list, reverse=True)
    dis_num_list = [(abs(num-n), num) for num in sorted_num_list]
    sorted_dis_num_list = sorted(dis_num_list, key = lambda x : x[0])
    
    return [x for _, x in sorted_dis_num_list]

# Best Code
def solution(numlist, n):
    answer = sorted(numlist,key = lambda x : (abs(x-n), n-x))
    return answer

'''
    key = lambda x : (abs(x-n), n-x) 라고 설정하면 
    abs(x-n)가 첫 번째 기준이고 이 기준을 충족할 경우 두 번째 기준 (n-x)를 충족하는 구조
'''
