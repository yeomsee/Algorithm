# My Code
def solution(num_list):
    odd_list, even_list = [], []
    for i in range(len(num_list)):
        if i%2 == 0:
            odd_list.append(num_list[i])
        else:
            even_list.append(num_list[i])
    
    if sum(odd_list) > sum(even_list):
        return sum(odd_list)
    else:
        return sum(even_list)