# My Code
def solution(my_list):
    row_num, col_num = len(my_list), len(my_list[0])
    if row_num > col_num: # 행의 수가 더 많은 경우
        for arr in my_list:
            arr.extend([0]*(row_num - col_num))
    else: # 열의 수가 더 많은 경우
        for _ in range(col_num - row_num):
            my_list.append([0] * (col_num))
        
    return my_list