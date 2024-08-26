# My Code
def solution(bin1, bin2):
    temp_str = str(int(bin1) + int(bin2))
    temp_list = list(temp_str)
    
    for i in range(len(temp_list)):
        if int(temp_list[-1-i]) >= 2:
            temp_list[-1-i] = str(int(temp_list[-1-i]) - 2)
            if i+1 == len(temp_list):
                temp_list.insert(0, '0')
            temp_list[-2-i] = str(int(temp_list[-2-i]) + 1)
    
    return ''.join(temp_list)

# Best Code
def solution(bin1, bin2):
    answer = bin(int(bin1,2) + int(bin2,2))[2:]
    return answer

'''
    int(value, base)
    : value를 base진법으로 표현함
'''
