# My Code
def solution(array):
    convert_num2count = {}
    for num in array:
        if num not in convert_num2count.keys():
            convert_num2count[num] = 1
        else:
            convert_num2count[num] += 1
    
    M = max(convert_num2count.values())
    max_list = [k for k, v in convert_num2count.items() if v == M]
    
    return max_list[0] if len(max_list) == 1 else -1 