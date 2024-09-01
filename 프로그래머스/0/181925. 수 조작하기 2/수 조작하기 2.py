# My Code
def solution(numLog):
    temp_dict = {1 : 'w', -1 : 's', 10 : 'd', -10 : 'a'}
    answer = [
        temp_dict[numLog[i+1] - numLog[i]]
        for i in range(len(numLog))
        if (i <= len(numLog) -2)
    ]
        
    return ''.join(answer)