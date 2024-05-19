def solution(rsp):
    win_dict = {'2' : '0', '0' : '5', '5' : '2'}
    
    answer = ''
    for string in rsp:
        answer += win_dict[string]
        
    return answer