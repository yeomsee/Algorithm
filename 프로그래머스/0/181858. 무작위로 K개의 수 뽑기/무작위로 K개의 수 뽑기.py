# My Code
def solution(arr, k):
    answer_list = []
    for num in arr:
        if num not in answer_list and len(answer_list) < k:
            answer_list.append(num)
    
    if (left := k - len(answer_list)) != 0:
        for _ in range(left):
            answer_list.append(-1)
    return answer_list

# Best Code
def solution(arr, k):
    ret = []
    for i in arr:
        if i not in ret:
            ret.append(i)
        if len(ret) == k:
            break

    return ret + [-1] * (k - len(ret))

'''
    내 풀이는 너무 경직돼서 푸는 느낌,,?
    좀 유연하게 풀어보자!
    생각! 생각! 생각!
'''
