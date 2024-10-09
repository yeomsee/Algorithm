# My Code
def solution(arr1, arr2):
    answer = []
    for x, y in zip(arr1, arr2):
        temp_list = [x[i]+y[i] for i in range(len(x))]
        answer.append(temp_list)
        
    return answer