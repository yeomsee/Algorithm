# My Code
def solution(array, n):
    dist_list = [abs(num - n) for num in array]
    min_dist = min(dist_list) # dist_list.min()는 아님에 주의!
    min_idx_list = [idx for idx, val in enumerate(dist_list) if val == min_dist]
    
    answer_list = []
    for i in min_idx_list:
        if len(min_idx_list) == 1:
            return array[i]
        else:
            answer_list.append(array[i])
    return min(answer_list)

# Best Code
def solution(array, n):
    array.sort()
    temp = []

    for i in array :
        temp.append( abs(n-i) )

    return array[temp.index(min(temp))]

'''
    이거 이외에도 한 줄짜리 코드가 있기는 한데,,
    사실 그렇게 코드를 작성하는 게 직관적일까? 라는 생각이 들어서
    어느 정도 길이가 있는 직관적인 코드를 들고 오게 됨.
'''
