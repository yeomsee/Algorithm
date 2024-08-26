# My Code
def solution(my_string):
    temp_list = my_string.split()
    
    answer = int(temp_list[0])
    
    for i in range(1, len(temp_list), 2):
        if temp_list[i] == '+':
            answer += int(temp_list[i+1])
        elif temp_list[i] == '-':
            answer -= int(temp_list[i+1])
        
        
        
            
    return answer