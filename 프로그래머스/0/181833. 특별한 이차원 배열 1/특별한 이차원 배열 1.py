# My Code
def solution(n):
    answer = []
    for i in range(n):
        temp_list = []
        for j in range(n):
            if i == j:
                temp_list.append(1)
            else:
                temp_list.append(0)
        answer.append(temp_list)
                
    return answer