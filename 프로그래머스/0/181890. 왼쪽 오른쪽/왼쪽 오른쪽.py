# My Code
def solution(str_list):    
    if "l" in str_list and "r" not in str_list:
        l_idx = str_list.index("l")
        return str_list[:l_idx]
    elif "l" not in str_list and "r" in str_list:
        r_idx = str_list.index("r")
        return str_list[r_idx+1:]
    elif "l" in str_list and "r" in str_list:
        l_idx = str_list.index("l")
        r_idx = str_list.index("r")
        if l_idx < r_idx:
            return str_list[:l_idx]
        else:
            return str_list[r_idx+1:]
    else:
        return []

# Best Code
def solution(str_list):
    for i in range(len(str_list)):
        if str_list[i]=='l': return str_list[:i]
        elif str_list[i]=='r': return str_list[i+1:]
    return []
