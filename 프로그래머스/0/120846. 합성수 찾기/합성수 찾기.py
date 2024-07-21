# My Code
def solution(n):
    answer_list = []
    for i in range(1, n+1):
        count = 0
        for x in range(1, i+1):
            if i%x == 0:
                count += 1
        if count >= 3:
            answer_list.append(x)
            
    return len(answer_list)