# My Code
def solution(scores):
    mean_list = [sum(score)/2 for score in scores]
    sorted_mean_list = sorted(mean_list, reverse=True)
    
    answer = [sorted_mean_list.index(x)+1 for x in mean_list]
    
    return answer