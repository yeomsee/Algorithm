# My Code
def solution(arr, queries):
    answer = []
    for (s, e, k) in queries:
        temp_list = [arr[i] for i in range(s, e+1) if arr[i] > k]
        if len(temp_list) == 0:
            answer.append(-1)
        else:
            answer.append(min(temp_list))
    return answer