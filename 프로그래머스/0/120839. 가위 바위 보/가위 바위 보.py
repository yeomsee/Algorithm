# My Code
def solution(rsp):
    win_dict = {'2' : '0', '0' : '5', '5' : '2'}
    
    answer = ''
    for string in rsp:
        answer += win_dict[string]
        
    return answer

# Best Code
def solution(rsp):
    d = {'0':'5','2':'0','5':'2'}
    return ''.join(d[i] for i in rsp)
