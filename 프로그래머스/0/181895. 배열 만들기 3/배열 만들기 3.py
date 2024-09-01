# My Code
def solution(arr, intervals):
    answer = []
    for interval in intervals:
        start, end = interval
        answer.extend(arr[start:end+1])
    
    return answer