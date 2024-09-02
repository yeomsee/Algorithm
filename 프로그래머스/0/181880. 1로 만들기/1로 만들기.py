# My Code
def solution(num_list):
    count = 0
    for num in num_list:
        while True:
            if num == 1:
                break
            num = num/2 if num%2 == 0 else (num-1)/2
            count += 1
                
    return count