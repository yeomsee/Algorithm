# My Code
def solution(num_list):
    even_str = ''.join([str(num) for num in num_list if num%2 == 0])
    odd_str = ''.join([str(num) for num in num_list if num%2 != 0])
    
    return int(even_str) + int(odd_str)