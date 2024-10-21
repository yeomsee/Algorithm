# My Code
def solution(s):
    blank_idx_list = [i for i in range(len(s)) if s[i] == " "]
    
    string_list = s.split()
    answer_list = []
    for string in string_list:
        temp_list = [string[i].upper() if i%2 == 0 else string[i].lower() for i in range(len(string))]
        answer_list.extend(temp_list)
        
    
    for idx in blank_idx_list:
        answer_list.insert(idx, " ")
    return ''.join(answer_list)